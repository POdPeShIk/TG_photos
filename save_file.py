import pathlib
import requests
import os.path
from urllib.parse import urlparse
from pathlib import Path


def format(url):
    p_url = urlparse(url)
    path = p_url.path
    extension = os.path.splitext(path)[1]
    return extension

def save(url,filename,path_name,api_key=None):
    os.makedirs(pathlib.Path(f"images/{path_name}"), exist_ok=True)
    payload = {"api_key":api_key }
    response = requests.get(url,  params=payload)
    response.raise_for_status()
    extension = format(url)
    path_two=pathlib.Path(f"images/{path_name}/image_{filename}{extension}")
    with open(f'{path_two}', 'wb') as file:
        file.write(response.content)
