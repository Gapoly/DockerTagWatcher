<p align='center'>
    <a href='https://hub.docker.com/' target="_blank" rel="noopener">
        <img src='https://github.com/user-attachments/assets/19b7eaaf-875e-4b63-96fd-5ee914fa54ae'/>
    </a>
</p>

# 🐳 1. What is DockerTagWatcher ?

DockerTagWatcher is a Python script that watches given images from the Docker Hub and send you a notification by email when a new stable version is released.


# 📚️ 2. The packages

### Necessary packages :




Those are the basics packages to make the script work. Python

- Python3
- Python3-requests
- Python3-schedule

### Recommended packages :

- Python3-poetry
- Tmux
- Git

## 📄 3. The installation

### Installation with Poetry (Recommended) :


- Ubuntu / Debian
```shell
sudo apt update && sudo apt install python3-poetry tmux git -y
```

Once the packages are installed, make you sure you are in the desired location of the desired folder location :

```shell
git clone https://github.com/Gapoly/DockerTagWatcher
cd DockerTagWatcher
poetry init
```

You will get prompts for initiating the Poetry environment. You can skip all of them by clicking "Enter" :

![image](https://github.com/user-attachments/assets/ba62903b-ffd5-4daf-87e5-ad64d1c5bf52)


```shell
poetry add requests schedule
```
## ⚙️ 4. The configuration

For this script to work, you'll need to modify these 2 files in dependencies :

- `SMTP.py`
- `docker_list.py`

### `SMTP.py` :

- You'll have to insert your credentials

```python
SMTP_SERVER = "smtp.server.com"
SMTP_PORT = 465  # 465 for SSL/TLS - 587 for STARTTLS
SENDER_EMAIL = "your_email@domain.com"
SENDER_PASSWORD = "your_password"
RECEIVER_EMAILS = [
    "recipient1@domain.com",
    "recipient2@domain.com"
    # Add new addresses
]
```

### `docker_list.py` :

- You'll have to put the images you want to follow

```python
DOCKER_IMAGES = [
    "library/image1",
    "library/image2"
]
```

Once you've done that. You can now execute the script.

# ✒️ 5. Execution

```shell
tmux new -s dockertagwatcher
```

```shell
poetry run python3 dockertagwatcher.py
```
- To quit the Tmux terminal without closing it :

`Ctrl + B, Then D`
