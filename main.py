#!/usr/bin/env python


import telegram
from flask import Flask, request

from config import BOT_TOKEN, PORT, HOST
from models.db_settings import db_session

app = Flask(__name__)


@app.teardown_request
def teardown_request(exception=None):
    db_session.remove()


@app.route('/bot_handler/<bot_token>', methods=['POST'])
def bot_handler(bot_token):
    bot = telegram.Bot(bot_token)
    update = telegram.update.Update.de_json(request.get_json(force=True), bot=bot)
    # Commands_Handler(update, bot).process_update(update)

    return 'OK'


def set_webhook(bot_token):
    bot = telegram.Bot(bot_token)
    bot.delete_webhook()
    res = bot.setWebhook(url='https://%s/bot_handler/%s' % (HOST, BOT_TOKEN))
    print('Bot is run' if res else 'failed for %s' % BOT_TOKEN)


if __name__ == '__main__':
    set_webhook(BOT_TOKEN)
    app.run(host='0.0.0.0',
            port=PORT,
            debug=True)
