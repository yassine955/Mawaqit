import pygame
import requests
import os


def play_audio(file_path):
    pygame.mixer.init()
    pygame.mixer.music.load(file_path)
    pygame.mixer.music.play()


def download_mp3(url):
    response = requests.get(url)
    file_path = "audio.mp3"

    with open(file_path, "wb") as file:
        file.write(response.content)

    return file_path


def main():
    input_path = input("Enter the audio file path or online MP3 link: ")

    if input_path.startswith("http://") or input_path.startswith("https://"):
        file_path = download_mp3(input_path)
    else:
        file_path = input_path

    if not os.path.exists(file_path):
        print("File not found.")
        return

    play_audio(file_path)

    print("Playing audio.")

    while pygame.mixer.music.get_busy():
        pass

    if file_path == "audio.mp3":
        os.remove(file_path)


if __name__ == "__main__":
    main()
