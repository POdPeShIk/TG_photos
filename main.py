import os
from dotenv import load_dotenv


from fetch_spacex_images import get_spacex_photos
from epic import get_epic_photos
from apod import get_thirty_links
from tg import go


if __name__ == "__main__":
  os.makedirs("images", exist_ok=True)
  load_dotenv(".env")
  token = os.environ['TELEGRAM_TOKEN']
  time = int(os.environ["WAITING_TIME"])
  chat_id = os.environ["TG_CHAT_ID"]
  url = os.environ["URL"]
  directory = os.environ["DIRECTORY"]  #Выберите папку (Если хотите рандомное фото из папки)
  api_key = os.environ['NASA_API_KEY']
  launch_id = os.environ['LAUNCH_ID']
  chat_id = os.environ["CHAT_ID"]
  get_thirty_links(api_key)
  get_epic_photos(api_key)
  get_spacex_photos(launch_id)
  go(chat_id, time, url)