import requests
import argparse
from save_file import save
from dotenv import load_dotenv


def get_spacex_photos(ids= "5eb87d47ffd86e000604b38a"):
    if ids =="5eb87d47ffd86e000604b38a":
        response = requests.get(f"https://api.spacexdata.com/v4/launches/{ids}")
        print(response)
    else:
        payload = {"flight_id": ids}
        response = requests.get(f"https://api.spacexdata.com/v4/launches", params=payload)
    response.raise_for_status()
    photos = response.json()
    photos = photos['links']['flickr']["original"]
    for photo_number, photo in enumerate(photos, start=1):
        filename = f"spacex_{photo_number}"
        save(photo, filename, "SPACE_X")


if __name__ == "__main__":
    load_dotenv(".env")
    parser = argparse.ArgumentParser(
        description='Описание что делает программа'
    )
    parser.add_argument('--id', help='Ваша фамилия')
    args = parser.parse_args()
    if args.id == None:
        get_spacex_photos()
    else:
        ids=args.id
        print(ids)
        get_spacex_photos(ids)
