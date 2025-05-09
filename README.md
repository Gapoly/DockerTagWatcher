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
- Python3-smtplib

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

You will get prompts for initiating the Poetry environment. You can skip all of them by clicking "Enter".

```shell
poetry add requests schedule smtplib
```
## 📑 4. The configuration

For this script to work, you'll need to modify these 2 files :

- `SMTP.py`
- `docker_list.py`