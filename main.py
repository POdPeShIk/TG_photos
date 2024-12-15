import os
from dotenv import load_dotenv

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
    directory = os.environ["DIRECTORY"]  # Выберите папку (Если хотите рандомное фото из папки)
    api_key = os.environ['NASA_API_KEY']
    launch_id = os.environ['LAUNCH_ID']
    get_thirty_links(api_key)
    images_epic=get_epic_photos(api_key)
    for image_number, image in enumerate(images_epic):
        save_epic_photos(image, image_number, api_key)
    get_spacex_photos(launch_id)
    print("j")
    start_code(chat_id, url, time)
