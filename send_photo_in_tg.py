import telegram
import os
import random
import time
from dotenv import load_dotenv


def main():
    load_dotenv()
    token = os.environ['TG_BOT_TOKEN']
    chat_id = os.environ['TG_CHAT_ID']
    bot = telegram.Bot(token=token)
    images = os.walk('images')
    for image in images:
        name_images = image[2]
    time_waiting = 144000
    while True:
        random.shuffle(name_images)
        for name_image in name_images:
            with open(f'images/{download_image}', 'rb') as file:
                bot.send_photo(chat_id=chat_id, photo=file)
            time.sleep(time_waiting)


if __name__ == "__main__":
    main()
