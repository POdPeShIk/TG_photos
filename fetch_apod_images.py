import requests
import os
import argparse
from dotenv import load_dotenv

from save_file import save


def get_links(api_key):
    payload = {"api_key": api_key, "count": 30}
    links = requests.get('https://api.nasa.gov/planetary/apod', params=payload)
    return links


def get_thirty_links(api_key, date = "today"):
    payload={"api_key": api_key,
        "date": date}
    links= get_links(api_key)
    links = links.json()
    for link_number, link in enumerate(links):
        image_url = link["url"]
        filename=f"apod_{link_number}"
        save(image_url , filename, "APOD",api_key)


if __name__ == "__main__":
    load_dotenv()
    api_key=os.environ['NASA_API_KEY']
    parser = argparse.ArgumentParser(
        description='Описание что делает программа'
    )
    parser.add_argument('--date', help='YYYY-MM-DD')
    args = parser.parse_args()
    if args.date:
        date = args.date
        get_thirty_links(api_key,date)
    else:
        get_thirty_links(api_key)


