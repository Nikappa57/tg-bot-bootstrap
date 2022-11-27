from telegram import InlineKeyboardMarkup, InlineKeyboardButton

from Bot.decorator import chattype, checkuser
from Bot.database.models import Users
from Bot.database import db


# start #
@checkuser.check()
def start(update, context, currentuser):
    keyboard = [
        [
            InlineKeyboardButton('Example', callback_data='hey')
        ]
    ]
    update.message.reply_text('Start', reply_markup=InlineKeyboardMarkup(keyboard))


# admin #
@chattype.private
@checkuser.check(adminrequired=True)
@checkuser.user_arg
def ban(update, context, currentuser, user):
    user.ban = True
    user.save()

    update.message.reply_text(
        'The user has been banned.'
    )


@chattype.private
@checkuser.check(adminrequired=True)
@checkuser.user_arg
def unban(update, context, currentuser, user):
    user.ban = False
    user.save()

    update.message.reply_text(
        'User unban with success.'
    )


@chattype.private
@checkuser.check(adminrequired=True)
def users(update, context, currentuser):
    update.message.reply_text('Users:\n{}'.format(
        "\n".join(f"{number} - {user}" for number, user in enumerate(db.session.query(Users).all()))))


@chattype.private
@checkuser.check(adminrequired=True)
@checkuser.user_arg
def admin(update, context, currentuser, user):
    user.admin = True
    user.save()
    
    update.message.reply_text(
        "The user has become an admin."
    )


@chattype.private
@checkuser.check(adminrequired=True)
@checkuser.user_arg
def unadmin(update, context, currentuser, user):
    user.admin = False
    user.save()

    update.message.reply_text(
        "The user has been demoted."
    )


@chattype.private
@checkuser.check(adminrequired=True)
@checkuser.user_arg
def info(update, context, currentuser, user):
    update.message.reply_text(
        str(user)
    )