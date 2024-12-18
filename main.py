import os
from dotenv import load_dotenv
import pathlib

from fetch_spacex_images import get_spacex_photos
from fetch_epic_images import get_epic_photos
from fetch_epic_images import save_epic_photos
from fetch_apod_images import get_thirty_links
from send_imgs_tg import start_code


if __name__ == "__main__":
    os.makedirs("images", exist_ok=True)
    load_dotenv(".env")
    token = os.environ['TELEGRAM_TOKEN']
    time = os.getenv("WAITING_TIME", 4)
    chat_id = os.environ["TG_CHAT_ID"]
    url = f'https://api.telegram.org/{token}/sendPhoto'
    directory = os.getenv("DIRECTORY",default=pathlib.Path("images/APOD/"))  # Выберите папку (Если хотите рандомное фото из папки)
    api_key = os.environ['NASA_API_KEY']
    launch_id = os.getenv('LAUNCH_ID', default = "today")
    get_thirty_links(api_key)
    images_epic=get_epic_photos(api_key, "today")
    for image_number, image in enumerate(images_epic):
        save_epic_photos(image, image_number, api_key)
    get_spacex_photos(launch_id)
    start_code(chat_id, time, token, directory)
