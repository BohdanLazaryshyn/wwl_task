import requests

from wwl_task.settings import BOT_TOKEN, CHAT_ID

bot_token = BOT_TOKEN
chat_id = CHAT_ID


def send_message(message):
    requests.get(
        f"https://api.telegram.org/bot{bot_token}/sendMessage",
        {"chat_id": chat_id, "text": message},
    )
