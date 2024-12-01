import requests
import os
from datetime import datetime
from download_image import download_image
from dotenv import load_dotenv


def get_epic_nasa_images(token):
    url = f'https://api.nasa.gov/EPIC/api/natural/image'
    count = 30
    params = {'count': 'count', 'api_key': token}
    response = requests.get(url, params=params)
    response.raise_for_status()
    for link in response.json():
        epic_date = datetime.fromisoformat(link["date"]).strftime("%Y/%m/%d")
        epic_name = link["image"]
        params = {'api_key' : f'{token}'}
        picture_link = requests.get(f'https://api.nasa.gov/EPIC/archive/natural/{epic_date}/png/{epic_name}.png', params=params)
        download_image(picture_link, f'epic_{epic_name}.png')


def main():
    load_dotenv()
    token = os.environ["NASA_KEY"]
    epics_nasa(token)


if __name__ == "__main__":
    main()
