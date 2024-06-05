import requests
import argparse
from save_file import save
from dotenv import load_dotenv
import os


def get_spacex_photos(api_key,ids= "5eb87d47ffd86e000604b38a"):
    if ids =="5eb87d47ffd86e000604b38a":
        response = requests.get(f"https://api.spacexdata.com/v4/launches/{ids}")
        response.raise_for_status()
    else:
        payload = {"flight_id": ids}
        response = requests.get(f"https://api.spacexdata.com/v4/launches", params=payload)
        response.raise_for_status()
    photos = response.json()
    photos = photos['links']['flickr']["original"]
    for photo_number, photo in enumerate(photos, start=1):
        filename = f"spacex_{photo_number}"
        save(photo, filename, "SPACE_X",api_key)


if __name__ == "__main__":
    load_dotenv(".env")
    api_key=os.environ['NASA_API_KEY']
    parser = argparse.ArgumentParser(
        description='Описание что делает программа'
    )
    parser.add_argument('--id', help='Ваша фамилия')
    args = parser.parse_args()
    if args.id:
        ids=args.id
        get_spacex_photos(api_key,ids)
    else:
        get_spacex_photos(api_key)