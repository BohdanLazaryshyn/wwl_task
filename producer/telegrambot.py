import requests


bot_token = "6077204161:AAGKxrXF7mMt7mYkljwVX_9R0c0-RkzSDRw"
chat_id = "422467834"


def send_message(message):
    requests.get(
        f"https://api.telegram.org/bot{bot_token}/sendMessage",
        {"chat_id": chat_id, "text": message},
    )
