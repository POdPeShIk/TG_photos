import os
from dotenv import load_dotenv


from fetch_spacex_images import get_spacex_photos
from epic import get_epic_photos
from apod import thirty_links
from tg import go


if __name__ == "__main__":
  os.makedirs("images", exist_ok=True)
  load_dotenv(".env")
  api_key = os.environ['API_KEY']
  id = "5eb87d47ffd86e000604b38a"
  time = int(input("Время в часах:"))
  chat_id="@testingmain"
  thirty_links(api_key)
  get_epic_photos(api_key)
  get_spacex_photos(id)
  go(chat_id, time)