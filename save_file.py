import requests
import os.path
from urllib.parse import urlparse


def format(url):
    p_url = urlparse(url)
    path = p_url.path
    extension = os.path.splitext(path)[1]
    return extension

def save(url,filename,path_name):
    os.makedirs(f"images/{path_name}", exist_ok=True)
    api_key=os.environ['API_KEY']
    payload = {"api_key":api_key }
    response = requests.get(url,  params=payload)
    response.raise_for_status()
    extension = format(url)
    with open(f"images/{path_name}/image_{filename}{extension}", 'wb') as file:
        file.write(response.content)
