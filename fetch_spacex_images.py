import requests
import argparse
from save_file import save_pic
from dotenv import load_dotenv


def get_spacex_photos(launch_id="5eb87d47ffd86e000604b38a"):
    response = requests.get(f"https://api.spacexdata.com/v4/launches/{launch_id}")
    response.raise_for_status()
    photos = response.json()
    photos = photos['links']['flickr']["original"]
    for photo_number, photo in enumerate(photos, start=1):
        filename = f"spacex_{photo_number}"
        save_pic(photo, filename, "SPACE_X")


if __name__ == "__main__":
    load_dotenv(".env")
    parser = argparse.ArgumentParser(
        description='Описание что делает программа'
    )
    parser.add_argument('--id', help='Ваша фамилия')
    args = parser.parse_args()
    if args.id:
        launch_id = args.id
        get_spacex_photos(launch_id)
    else:
        get_spacex_photos()