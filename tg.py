import telegram
import os
from dotenv import load_dotenv
import time
import requests
import random


def send_photo(chat_id, photo_path):
    url=f"https://api.telegram.org/bot6952317922:AAFaDoQ_pmKZrOZipgcpS1xGMfwMjdpyVWc/sendPhoto"
    files = {'photo': open(photo_path, 'rb')}
    data = {'chat_id': chat_id}
    response = requests.post(url,   files=files, data=data)
    json_response = response.json()
    return json_response


def go(xtime):
    directory = os.environ["DIRECTORY"] #Выберите папку
    photos = os.listdir(directory)
    xtime=xtime*3600
    random.shuffle(photos)
    while True:
        for photo in photos:
            path=directory+photo
            send_photo(chat_id, path)
            time.sleep(xtime)




if __name__ == "__main__":
    load_dotenv(".env")
    token=os.environ['TOKEN']
    xtime=int(os.environ["XTIME"])
    chat_id= "@testingmain"
    bot = telegram.Bot(token="7023144175:AAFNrL2XdYfO1olmN8gDxc7py26eInzOw6g")
    go(xtime)