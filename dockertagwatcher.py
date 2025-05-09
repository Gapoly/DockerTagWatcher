import requests
import smtplib
import schedule
import time
import os

from dependencies.docker_list import DOCKER_IMAGES
from dependencies.SMTP import *

LAST_VERSIONS_DIR = "last_versions"

def get_latest_stable_tag(image):
    """Fetch the latest stable tag for a Docker image from Docker Hub."""
    url = f"https://hub.docker.com/v2/repositories/{image}/tags?page_size=100"
    response = requests.get(url)
    response.raise_for_status()
    tags = response.json()["results"]
    stable_tags = [tag["name"] for tag in tags if all(x not in tag["name"] for x in ["rc", "beta", "alpha"])]
    stable_tags.sort(reverse=True)
    return stable_tags[0] if stable_tags else None

def send_email_notification(image, new_version):
    """Send an email notification to multiple recipients."""
    subject = f"New stable version detected: {image}:{new_version}"
    body = f"A new stable version of the image {image} is available: {new_version}"
    message = f"Subject: {subject}\n\n{body}"

    with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
        server.starttls()
        server.login(SENDER_EMAIL, SENDER_PASSWORD)
        server.sendmail(
            SENDER_EMAIL,
            RECEIVER_EMAILS,
            message
        )

def check_new_versions():
    """Check for new versions for all monitored images."""
    if not os.path.exists(LAST_VERSIONS_DIR):
        os.makedirs(LAST_VERSIONS_DIR)
    for image in DOCKER_IMAGES:
        try:
            latest_version = get_latest_stable_tag(image)
            image_file = os.path.join(LAST_VERSIONS_DIR, image.replace("/", "_") + ".txt")
            try:
                with open(image_file, "r") as f:
                    last_known_version = f.read().strip()
            except FileNotFoundError:
                last_known_version = None

            if latest_version and latest_version != last_known_version:
                send_email_notification(image, latest_version)
                with open(image_file, "w") as f:
                    f.write(latest_version)
        except Exception:
            # Errors are silently ignored to prevent blocking the loop
            pass

# Daily scheduling
schedule.every().day.at("08:00").do(check_new_versions)

# (Optional) Remove the next line for zero output
print("Script is running. Press Ctrl+C to stop.")

while True:
    schedule.run_pending()
    time.sleep(60)