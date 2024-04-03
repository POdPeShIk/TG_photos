import requests
from save_file import save
from dotenv import load_dotenv


def get_spacex_photos(id):
    response = requests.get(f"https://api.spacexdata.com/v4/launches/{id}")
    response.raise_for_status()
    photos = response.json()
    photos = photos['links']['flickr']["original"]
    for photo_number, photo in enumerate(photos, start=1):
        response = requests.get(photo)
        filename = f"spacex_{photo_number}"
        save(photo, filename, "SPACE_X")


if __name__ == "__main__":
    id = "5eb87d47ffd86e000604b38a"
    load_dotenv(".env")
    get_spacex_photos(id)
