from datetime import datetime, timedelta
import time
from typing import Any, Dict, TypedDict
from pygame import mixer
import requests
from bs4 import BeautifulSoup
import re
import time
import json
from functions.scraper import get_prayer_times_to_json, get_current_time

from functions.get_config import get_config

# CONFIG SETTINGS
mixer.init()
config = get_config()
response = requests.get(config["uri"])
adhan_sound = "audio/azan5.wav"

get_prayer_times_to_json(response, config)


def check_prayer_times():

    print(
        f"------------------------------XXXXXXXXXXXXXXXXXXX--------------------------"
    )
    list_of_times = get_current_time()

    current_time = datetime.now().strftime("%H:%M")

    time_obj = datetime.strptime(list_of_times[0], "%H:%M")
    new_time_obj_minus_30 = time_obj - timedelta(minutes=40)
    new_time_obj_minus_30_str = new_time_obj_minus_30.strftime("%H:%M")

    print(f"Current time: {current_time}")
    print(f"Today's Times: {list_of_times}")
    print(f"Today's Imsaak Time: {new_time_obj_minus_30_str}")

    # Check if current time is present in the list of prayer times
    if current_time in list_of_times:
        print("Current time is present in the list of prayer times.")
        mixer.music.load(adhan_sound)
        mixer.music.play()

    if current_time == new_time_obj_minus_30_str:
        print(
            f"Current Time: {current_time} -> Imsaak Time: {new_time_obj_minus_30_str}"
        )
        for _ in range(3):
            mixer.music.load("audio/short.wav")
            mixer.music.play()
            time.sleep(15)

    else:
        print("Current time is not present in the list of prayer times.")


check_prayer_times()

while True:

    now = datetime.now()
    seconds_until_next_minute = 60 - now.second

    time.sleep(seconds_until_next_minute)

    check_prayer_times()
