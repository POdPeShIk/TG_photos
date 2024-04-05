import requests
import argparse
from save_file import save
from dotenv import load_dotenv


def get_spacex_photos(ids):
    response = requests.get(f"https://api.spacexdata.com/v4/launches/{ids}")
    response.raise_for_status()
    photos = response.json()
    if ids == "latest":
        print(photos)
    else:
        photos = photos['links']['flickr']["original"]
    for photo_number, photo in enumerate(photos, start=1):
        response = requests.get(photo)
        filename = f"spacex_{photo_number}"
        save(photo, filename, "SPACE_X")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description='Описание что делает программа'
    )
    parser.add_argument('--id', help='ID запуска', required=False)
    args = parser.parse_args()
    if not args.id:
        ids = "latest"
    else:
        ids = args.id
    load_dotenv(".env")
    get_spacex_photos(ids)
