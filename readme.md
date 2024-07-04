# CTF idea 1 - 10 points

## Description

This is a simple CTF idea for beginners. The flag is hidden in secret/flag.txt file.

## Challenge

The flag is hidden in secret/flag.txt file. Find the flag. But how?

Installation on new system

You need to install docker and ttyd on your system. 

```bash
sudo apt update
sudo apt install docker.io ttyd -y
```

On system wide

```bash 
git clone
cd CTF-idea-1
pip install -r requirements.txt
python3 app.py 
OR 
flask run --host=0.0.0.0 --port=80
```

With venv 

```bash
git clone
cd CTF-idea-1
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python3 app.py
```