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


def get_pictures_of_the_days(token):
    url = f'https://api.nasa.gov/planetary/apod'
    count = 30
    params = {'count': 'count', 'api_key': token}
    response = requests.get(url, params=params)
    response.raise_for_status()
    for link in response.json():
        if links.get("media_type") == "image":
            picture_link = links['url'] or links['hdurl']
        name, extension = find_extension(picture_link)
        download_image(picture_link, f"{name}{extension}")


def main():
    load_dotenv()
    token = os.environ['NASA_KEY']
    picture_of_the_day(token)


if __name__ == "__main__":
    main()
