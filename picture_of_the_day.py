import requests
from download_image import download_image
import os
from urllib.parse import unquote, urlparse
from dotenv import load_dotenv


def find_extension(url):
    decoded_url = unquote(url)
    parsed_url = urlparse(decoded_url)
    head, full_name = os.path.split(parsed_url.path)
    name, extension = os.path.splitext(full_name)
    return name, extension


def picture_of_the_day(token):
    url = f'https://api.nasa.gov/planetary/apod?api_key={token}'
    params = {'count': 30}
    response = requests.get(url, params=params)
    response.raise_for_status()
    for links in response.json():
        if links.get("media_type") == "image":
            links_of_pictures = links['url'] or links['hdurl']
        name, extension = find_extension(links_of_pictures)
        download_image(links_of_pictures, f"{name}{extension}")


def main():
    token = os.environ['TOKEN_FOR_URL']
    picture_of_the_day(token)
    load_dotenv()

if __name__ == "__main__":
    main()
