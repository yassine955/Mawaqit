import requests
import json
import datetime
import time
from pygame import mixer

# Initialize pygame.mixer
mixer.init()

# Load the schedule from the JSON
with open("schedule.json", "r") as file:
    schedule = json.load(file)["schedule"]

print("Script started")

while True:
    try:
        # Get the current date and time
        current_datetime = datetime.datetime.now()

        # Get the current day number (1-31)
        current_day_number = current_datetime.day

        # Get the current time in HH:MM format
        current_time = current_datetime.strftime("%H:%M")

        print(f"Current date: {current_day_number}, time: {current_time}")

        # Find the entry for the current day in the schedule
        current_day_schedule = next(
            (
                day_schedule
                for day_schedule in schedule
                if day_schedule["day_number"] == current_day_number
            ),
            None,
        )

        if current_day_schedule:
            print(current_day_schedule["times"][:4] + current_day_schedule["times"][5:])
            # Check if the current time matches any time in the schedule for the current day (excluding the 5th value)
            if (
                current_time
                in current_day_schedule["times"][:4] + current_day_schedule["times"][5:]
            ):
                print("It's time!")
                mixer.music.load("azan5.wav")
                mixer.music.play()

        # Wait for the next minute
        time.sleep(60 - current_datetime.second)

    except KeyboardInterrupt:
        # Exit the loop if Ctrl+C is pressed
        break
