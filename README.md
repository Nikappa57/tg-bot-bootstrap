# Telegram Bot Boostrap

![GitHub Pipenv locked Python version](https://img.shields.io/github/pipenv/locked/python-version/Nikappa57/tg-bot-bootstrap?style=for-the-badge) ![GitHub Pipenv locked dependency version](https://img.shields.io/github/pipenv/locked/dependency-version/Nikappa57/tg-bot-bootstrap/python-telegram-bot?style=for-the-badge) ![GitHub Pipenv locked dependency version](https://img.shields.io/github/pipenv/locked/dependency-version/Nikappa57/tg-bot-bootstrap/sqlalchemy?style=for-the-badge) ![GitHub code size in bytes](https://img.shields.io/github/languages/code-size/Nikappa57/tg-bot-bootstrap?style=for-the-badge) ![GitHub last commit](https://img.shields.io/github/last-commit/Nikappa57/tg-bot-bootstrap?style=for-the-badge) ![GitHub](https://img.shields.io/github/license/Nikappa57/tg-bot-bootstrap?style=for-the-badge)

A simple start template to create your telegram bots.

## Features
- basic **commands**
ban, unban, add or remove admin, users list and user info
- an instance of the user in each function
- **error** message functions
- ready for **buttons** and **inline mode**
- a base **database** already connected
- useful decorator

## Installation
1. Clone this repo: 
```console
git clone https://github.com/Nikappa57/tg-bot-bootstrap.git
```
2. Install requirements.
```console
pip install -r requirements
```
or
```console
pipenv install
```
Create `.env` with your bot token 
```
TOKEN=yourtoken
```
Now you should be able to start your bot.
```console
python run.py
```

## How to use
#### Commands
add your commands in `commands.py` and they will be added automatically with the name given to the functions.
#### Decorators
```python
@check(adminrequired=False)
```

Check if the user is new, if he is banned, if he has changed his name and username and update them in the database.

IMPORTANT TO PLACE IT ON ALL CONTROLS AS FIRST DECORATOR.

`adminrequired=True` Check if the user is admin, if not send an error message in chat `Bot.errors.admin_required_error`

---

```python
@user_arg
```
Serves in all commands where you need to edit/recall another user
Supports the syntax `"/command chat_id"` and `"/command @username"`.
Also supports `reply_to_message`.

---

```python
@group
```
```python
@private
```
Useful for restricting the function only to groups or private chat.

## Where I used it

- [account-shop-bot](https://github.com/Nikappa57/account-shop-bot.git)
- [tg-duel-bot](https://github.com/Nikappa57/tg-duel-bot)

- [ABS-Scanner](https://github.com/Nikappa57/ABS-Scanner/tree/main/Api%20ABStool%20Bot)