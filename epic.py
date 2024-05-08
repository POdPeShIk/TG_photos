import requests
from dotenv import load_dotenv
import os
import argparse


from save_file import save


def get_epic_photos(api_key, date ="today"):
    if date == "today":
        payload = {"api_key":api_key }
        images = requests.get(f"https://api.nasa.gov/EPIC/api/natural/images", params=payload)
    else:
        payload = {"api_key":api_key,
                   "date": date}
        images = requests.get(f"https://api.nasa.gov/EPIC/api/natural", params=payload)
    images=images.json()
    for image in images:
        photo=image["image"]
        date=photo.replace("epic_1b_","")
        year=date[0:4]
        month=date[4:6]
        day=date[6:8]
        time=date[8:12]
        img_url = f"https://api.nasa.gov/EPIC/archive/natural/{year}/{month}/{day}/png/{photo}.png"
        filename=f"EPIC_{year}.{month}.{day}.{time}"
        save(img_url, filename, "EPIC")


if __name__ == "__main__":
    load_dotenv(".env")
    api_key=os.environ['API_KEY']
    parser = argparse.ArgumentParser(
        description='Описание что делает программа'
    )
    parser.add_argument('--date', help='YYYY-MM-DD')
    args = parser.parse_args()
    if args.date == None:
        get_epic_photos(api_key)
    else:
        date = args.date
        print(date)
        get_epic_photos(api_key, date)
