from datetime import datetime
import time
from pygame import mixer
import requests
from bs4 import BeautifulSoup


# Initialize pygame.mixer
mixer.init()

# Global variable to track the current audio file
current_audio = "adhan.mp3"


# Function to parse time string to datetime object
def parse_time(time_str):
    return datetime.strptime(time_str, "%H:%M")


# Function to check if current time is in the list of prayer times
def check_prayer_times():
    global current_audio

    # Get current time
    current_time = datetime.now().strftime("%H:%M")

    url = "https://www.al-yaqeen.com/gebedstijden/"
    cookies = {"currentCity": "29263"}

    response = requests.get(url, cookies=cookies)
    soup = BeautifulSoup(response.text, "html.parser")

    # Find the specific table row containing the prayer times
    prayer_table_row = soup.find("tr", class_="prayer-table__day current")

    # Extract all the prayer times from the specified row
    times = [td.get_text(strip=True) for td in prayer_table_row.find_all("td")]

    # Remove the second element from the list
    if len(times) >= 2:
        del times[1]

    print(times)

    # Check if current time is present in the list of prayer times
    if current_time in times:
        print("Current time is present in the list of prayer times.")
        mixer.music.load(current_audio)
        mixer.music.play()

        # Toggle the audio file for the next call
        if current_audio == "adhan.mp3":
            current_audio = "azan5.wav"
        else:
            current_audio = "adhan.mp3"
    else:
        print("Current time is not present in the list of prayer times.")


while True:

    now = datetime.now()
    seconds_until_next_minute = 60 - now.second
    time.sleep(seconds_until_next_minute)
    check_prayer_times()
