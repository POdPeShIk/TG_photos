import os
from dotenv import load_dotenv


from fetch_spacex_images import get_spacex_photos
from epic import get_epic_photos
from apod import thirty_links
from tg import go


if __name__ == "__main__":
  load_dotenv(".env")
  token = os.environ['TELEGRAM_TOKEN']
  time = int(os.environ["WAITING_TIME"])
  chat_id = os.environ["TG_CHAT_ID"]
  url = os.environ["URL"]
  api_key = os.environ['NASA_API_KEY']
  directory = os.environ["DIRECTORY"]  #Выберите папку (Если хотите рандомное фото из папки)
  os.makedirs("images", exist_ok=True)
  load_dotenv(".env")
  api_key = os.environ['NASA_API_KEY']
  id = "5eb87d47ffd86e000604b38a"
  chat_id = os.environ["CHAT_ID"]
  thirty_links(api_key)
  get_epic_photos(api_key)
  get_spacex_photos(api_key,id)
  go(chat_id, time, url)
  print("УСЁ")