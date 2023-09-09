import requests
from bs4 import BeautifulSoup
from pygame import mixer
import time
import datetime

# Set the URL and the cookie value
url = "https://www.al-yaqeen.com/gebedstijden/"
cookies = {"currentCity": "29263"}

# Initialize pygame.mixer
mixer.init()

print("script started")

while True:
    try:
        # Calculate the time until the next minute
        current_time = datetime.datetime.now()
        seconds_until_next_minute = 60 - current_time.second

        # Wait for the next minute
        time.sleep(seconds_until_next_minute)

        # Send a GET request with the cookie
        response = requests.get(url, cookies=cookies)

        # Check if the request was successful
        if response.status_code == 200:
            # Parse the HTML content of the page
            soup = BeautifulSoup(response.text, "html.parser")

            # Find the table row with the class "prayer-table__day current"
            current_row = soup.find("tr", class_="prayer-table__day current")

            if current_row:
                # Extract all the <td> elements within the row except the second one
                time_elements = current_row.find_all("td")
                time_elements.pop(1)  # Remove the second element

                # Get the current time in HH:MM format
                current_time = datetime.datetime.now().strftime("%H:%M")

                for time_element in time_elements:
                    print(time_element.get_text(strip=True))
                    print(time_element.get_text(strip=True) == current_time)

                # Check if the extracted times match the current time
                if any(
                    time_element.get_text(strip=True) == current_time
                    for time_element in time_elements
                ):
                    print("It's time to pray!")

                    # Play the "beep.wav" sound
                    mixer.music.load("azan5.wav")
                    mixer.music.play()

    except KeyboardInterrupt:
        # Exit the loop if Ctrl+C is pressed
        break
