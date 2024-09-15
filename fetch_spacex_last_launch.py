import requests
from download_image import download_image


def fetch_spacex_last_launch():
    url = 'https://api.spacexdata.com/v5/launches/5eb87d47ffd86e000604b38a'
    response = requests.get(url)
    response.raise_for_status()
    links = response.json()["links"]["flickr"]["original"]
    for img_number, link in enumerate(links):
        download_image(link, 'spacex_' + str(img_number) + '.jpg')


def main():
    fetch_spacex_last_launch()


if __name__ == "__main__":
    main()
