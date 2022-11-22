from uuid import uuid4

from telegram import InlineQueryResultArticle, InputTextMessageContent, \
    InlineKeyboardMarkup, InlineKeyboardButton

from Bot.decorator import checkuser


@checkuser.check()
def inline_mode(update, context, currentuser):
    message = 'hey'

    update.inline_query.answer([
        InlineQueryResultArticle(
            id=uuid4(),
            title='Hello',
            description='Nice Desc',
            input_message_content=InputTextMessageContent(message))
    ], cache_time=0)