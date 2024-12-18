import requests
from dotenv import load_dotenv
import os
import argparse
import datetime

from save_file import save_pic


def get_epic_photos(api_key, date):
    if date == "today":
        payload = {"api_key": api_key}
        images = requests.get(f"https://api.nasa.gov/EPIC/api/natural/images", params=payload)
        images.raise_for_status()
    else:
        payload = {"api_key": api_key,
                   "date": date}
        images = requests.get(f"https://api.nasa.gov/EPIC/api/natural", params=payload)
        images.raise_for_status()
    images = images.json()
    return images


def save_epic_photos(image, image_number, api_key):
    photo = image["image"]
    pic_date = image["date"].split()[0]
    pict_date = datetime.datetime.strptime(pic_date, "%Y-%m-%d")
    pict_date = pict_date.strftime("%Y/%m/%d")
    img_url = f"https://api.nasa.gov/EPIC/archive/natural/{pict_date}/png/{photo}.png"
    filename = f"EPIC_{pic_date}_{image_number}"
    save_pic(img_url, filename, "EPIC", api_key)


if __name__ == "__main__":
    load_dotenv(".env")
    api_key = os.environ['NASA_API_KEY']
    parser = argparse.ArgumentParser(
        description='Описание что делает программа'
    )
    parser.add_argument('--date', help='YYYY-MM-DD',default="today")
    args = parser.parse_args()
    date = args.date
    get_epic_photos(api_key, date)
