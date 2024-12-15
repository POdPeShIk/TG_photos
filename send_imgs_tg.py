import telegram
import pathlib
import os
from dotenv import load_dotenv
import time
import requests
import random
import argparse
import logging


def send_photo(chat_id, photo_path):
    with open(photo_path, 'rb') as file:
        files = {'photo': file}
        data = {'chat_id': chat_id}
        response = requests.post(url = f'https://api.telegram.org/bot{token}/sendPhoto', data=data, files=files )
        response.raise_for_status()
        response = response.json()
        return response


def start_code(chat_id, xtime, directory=pathlib.Path("images/APOD/")):
    photos = os.listdir(directory)
    xtime = xtime * 3600
    while True:
        random.shuffle(photos)
        for photo in photos:
            xpath = pathlib.Path(directory,photo)
            send_photo(chat_id, xpath)
            time.sleep(xtime)


if __name__ == "__main__":
    load_dotenv()
    token = os.environ['TELEGRAM_TOKEN']
    xtime = int(os.getenv("WAITING_TIME", default=4))
    chat_id = os.environ["TG_CHAT_ID"]
    parser = argparse.ArgumentParser(
        description='Отправление фотографий в тг'
    )
    parser.add_argument('--path', help='Path of photo')
    args = parser.parse_args()
    if args.path:
        path = args.path
        send_photo(chat_id, path)
        start_code(chat_id, xtime)
    else:
        start_code(chat_id, xtime)
