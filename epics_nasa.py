import requests
import os
from datetime import datetime
from download_image import download_image
from dotenv import load_dotenv


def get_epics_nasa(token):
    url = f'https://api.nasa.gov/EPIC/api/natural/image'
    params = {'count': 30, 'api_key': token}
    response = requests.get(url, params=params)
    response.raise_for_status()
    for links in response.json():
        epic_date = datetime.fromisoformat(links["date"]).strftime("%Y/%m/%d")
        epic_name = links["image"]
        link_of_pictures = f'https://api.nasa.gov/EPIC/archive/natural/{epic_date}/png/{epic_name}.png?api_key={token}'
        download_image(link_of_pictures, f'epic_{epic_name}.png')


def main():
    load_dotenv()
    token = os.environ["NASA_KEY"]
    epics_nasa(token)


if __name__ == "__main__":
    main()
