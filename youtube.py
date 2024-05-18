import os
import sys
import requests
import pygame
import tempfile
from pygame import mixer

# Initialize pygame mixer
pygame.init()
mixer.init()


def download_mp3(url):
    try:
        response = requests.get(url, stream=True)
        response.raise_for_status()

        # Create a temporary file to store the downloaded mp3
        temp_dir = tempfile.gettempdir()
        temp_mp3_file = os.path.join(temp_dir, "temp_audio.mp3")

        with open(temp_mp3_file, "wb") as f:
            for chunk in response.iter_content(chunk_size=8192):
                f.write(chunk)

        return temp_mp3_file
    except Exception as e:
        print(f"An error occurred while downloading the file: {e}")
        return None


def play_mp3(file_path):
    try:
        # Load the mp3 file
        mixer.music.load(file_path)
        # Play the mp3 file
        mixer.music.play()

        # Keep the script running until the music stops
        while mixer.music.get_busy():
            pygame.time.Clock().tick(10)

        print("Playback finished.")
    except Exception as e:
        print(f"An error occurred while playing the file: {e}")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script.py <link to MP3 URL>")
        sys.exit(1)

    file_or_url = sys.argv[1]

    # Check if it's a URL
    if file_or_url.startswith("http://") or file_or_url.startswith("https://"):
        # Download the MP3 file
        mp3_file = download_mp3(file_or_url)
    else:
        # Use the local file path directly
        mp3_file = file_or_url

    # Play the MP3 file if it's successfully downloaded or available
    if mp3_file:
        print("Playing audio...")
        play_mp3(mp3_file)

        # Optionally, delete the temporary audio file after playing
        if file_or_url.startswith("http://") or file_or_url.startswith("https://"):
            os.remove(mp3_file)
            print("Temporary file deleted.")
    else:
        print("Failed to retrieve the MP3 file.")
