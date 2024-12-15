import pathlib
import requests
import os.path
from urllib.parse import urlparse
from pathlib import Path


def get_pic_format(url):
    p_url = urlparse(url)
    path = p_url.path
    extension = os.path.splitext(path)[1]
    return extension


def save_pic(url, filename, path_name, api_key=None):
    Path(f"images/{path_name}").mkdir(exist_ok=True)
    payload = {"api_key": api_key}
    response = requests.get(url, params=payload)
    response.raise_for_status()
    extension = get_pic_format(url)
    image_path = pathlib.Path(f"images/{path_name}/image_{filename}{extension}")
    with open(f'{image_path}', 'wb') as file:
        file.write(response.content)
