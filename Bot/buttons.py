import re

from Bot.decorator import checkuser, chattype
from Bot.database import db
from Bot.database.models import Users


@checkuser.check()
def button(update, context, currentuser) :
    query = update.callback_query
    data = query.data

    query.answer("Hey!")
