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
adhan_sound = "audio/med.wav"

get_prayer_times_to_json(response, config)

time_format = "%H:%M"


def check_prayer_times():

    print(
        f"------------------------------XXXXXXXXXXXXXXXXXXX--------------------------"
    )

    current_time = datetime.now().strftime("%H:%M")

    list_of_times = get_current_time()

    second_time = datetime.strptime(list_of_times[1], time_format)

    # Subtract 1 hour and 30 minutes
    new_time = second_time - timedelta(hours=1, minutes=30)

    # Convert the new time back to a string
    new_time_str = new_time.strftime(time_format)

    # Remove the second value and make the new time the first value
    list_of_times[1] = list_of_times[0]
    list_of_times[0] = new_time_str
    list_of_times.pop(1)

    print(f"Today's Times: {list_of_times}")

    # Check if current time is present in the list of prayer times
    if current_time in list_of_times:
        print("Current time is present in the list of prayer times.")
        mixer.music.load(adhan_sound)
        mixer.music.play()

    else:
        print("Current time is not present in the list of prayer times.")


check_prayer_times()

while True:

    now = datetime.now()
    seconds_until_next_minute = 60 - now.second

    time.sleep(seconds_until_next_minute)

    check_prayer_times()
