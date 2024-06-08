import telegram
import os
from dotenv import load_dotenv
import time
import requests
import random
import argparse


def send_photo(chat_id, photo_path,url):
    with open(photo_path, 'rb') as file:
      files = {'photo': file}
      data = {'chat_id': chat_id}
      response = requests.post(url,   files=files, data=data)
      response = response.json()
      return response


def go(chat_id, xtime,url, directory="images/APOD/"):
    photos = os.listdir(directory)
    xtime=xtime*3600
    while True:
        random.shuffle(photos)
        for photo in photos:
            xpath=directory+photo
            send_photo(chat_id, xpath, url)
            time.sleep(xtime)


if __name__ == "__main__":
    load_dotenv(".env")
    token = os.environ['TELEGRAM_TOKEN']
    url = os.environ["URL"]
    xtime = int(os.environ["WAITING_TIME"])
    chat_id = os.environ["TG_CHAT_ID"]
    bot = telegram.Bot(token=token)
    parser = argparse.ArgumentParser(
        description='Описание что делает программа'
    )
    parser.add_argument('--path', help='Path of photo')
    args = parser.parse_args()
    if args.path:
        path = args.path
        print(path)
        send_photo(chat_id, path, url)
        go(chat_id,xtime, url)
    else:
        go(chat_id,xtime, url)