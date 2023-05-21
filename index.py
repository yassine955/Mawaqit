import requests
from bs4 import BeautifulSoup
from datetime import datetime, time
import time as t

from pathlib import Path

import pygame

pygame.init()


print("start")
print(datetime.now().time().replace(second=0, microsecond=0).strftime("%H:%M"))

try:
    my_sound = pygame.mixer.Sound("beep.mp3")
    my_sound.play()
except pygame.error as e:
    print("Error playing audio:", e)


def fetch_prayer_times():
    # Send a GET request to the website
    url = "https://www.al-yaqeen.com/gebedstijden/"
    response = requests.get(url)

    # Parse the HTML content using BeautifulSoup
    soup = BeautifulSoup(response.content, "html.parser")

    # Find the table row with class "current"
    table_row = soup.find("tr", class_="prayer-table__day current")

    # Extract the prayer times from the table row
    prayer_times = [td.get_text(strip=True) for td in table_row.find_all("td")]

    # Convert prayer times to datetime objects without seconds
    prayer_times = [
        datetime.strptime(time_str, "%H:%M").time().strftime("%H:%M")
        for time_str in prayer_times
    ]

    return prayer_times


# Fetch and scrape the website initially
prayer_times = fetch_prayer_times()

# Remove the second value from the prayer times list if it exists
if len(prayer_times) >= 2:
    prayer_times.pop(1)

print(prayer_times)

# Set the target time for fetching and scraping
target_time = datetime.now().replace(hour=0, minute=10, second=0, microsecond=0).time()

# Calculate the remaining seconds until the next minute
remaining_seconds = (60 - datetime.now().second) % 60

# Delay until the next minute
t.sleep(remaining_seconds)


# Check if it's time for fetching and scraping
while True:
    current_time = (
        datetime.now().time().replace(second=0, microsecond=0).strftime("%H:%M")
    )
    print(current_time)

    if current_time == target_time:
        prayer_times = fetch_prayer_times()
        if len(prayer_times) >= 2:
            prayer_times.pop(1)

        print("Prayer times fetched and scraped.")

    if current_time in prayer_times:
        print(f"It's time for prayer: {current_time}")
        # Play audio file when it's time for prayer
        # playsound("azan5.mp3")

        x = pygame.mixer.Sound("azan5.mp3")

        x.play()

    else:
        # playsound("beep.mp3")
        print(f"Not time: {current_time}")

    # Delay for 1 minute before checking again
    t.sleep(60)
