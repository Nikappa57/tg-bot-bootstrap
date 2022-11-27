# Telegram Bot Boostrap

![GitHub Pipenv locked Python version](https://img.shields.io/github/pipenv/locked/python-version/Nikappa57/tg-bot-bootstrap?style=for-the-badge) ![GitHub Pipenv locked dependency version](https://img.shields.io/github/pipenv/locked/dependency-version/Nikappa57/tg-bot-bootstrap/python-telegram-bot?style=for-the-badge) ![GitHub Pipenv locked dependency version](https://img.shields.io/github/pipenv/locked/dependency-version/Nikappa57/tg-bot-bootstrap/sqlalchemy?style=for-the-badge) ![GitHub code size in bytes](https://img.shields.io/github/languages/code-size/Nikappa57/tg-bot-bootstrap?style=for-the-badge) ![GitHub last commit](https://img.shields.io/github/last-commit/Nikappa57/tg-bot-bootstrap?style=for-the-badge)

A simple start template to create your telegram bots

## Features
- basic **commands**
ban, unban, add or remove admin, users list and user info
- **error** message functions
- ready for **buttons** and **inline mode**
- a base **database** already connected
- useful decorator

## Installation
1. Clone this repo: 
```console
git clone https://github.com/Nikappa57/tg-bot-bootstrap.git
```
2. Install requirements
```
pip install -r requirements
```
or
```
pipenv install
```
Create `.env` with your bot token 
```
TOKEN=yourtoken
```
Now you should be able to start your bot
```console
python run.py
```

## How to use
#### Commands
add your commands in `commands.py` and they will be added automatically with the name given to the functions
#### Decorators
```python
@check(adminrequired=False)
```

Check if the user is new, if he is banned, if he has changed his name and username and update them in the database
IMPORTANT TO PLACE IT ON ALL CONTROLS AS FIRST DECORATOR

`adminrequired=True` Check if the user is admin, if not send an error message in chat `Bot.errors.admin_required_error`
