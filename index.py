from datetime import datetime
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

list_of_times = get_current_time()

print(list_of_times)


def check_prayer_times():

    current_time = datetime.now().strftime("%H:%M")

    # Check if current time is present in the list of prayer times
    if current_time in list_of_times:
        print("Current time is present in the list of prayer times.")
        mixer.music.load(adhan_sound)
        mixer.music.play()

    else:
        print("Current time is not present in the list of prayer times.")


while True:

    now = datetime.now()
    seconds_until_next_minute = 60 - now.second

    time.sleep(seconds_until_next_minute)

    check_prayer_times()
