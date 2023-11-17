from pytube import YouTube
import sys
import os
from pathlib import Path
import subprocess


def open_explorer(path):
    FILEBROWSER_PATH = os.path.join(os.getenv('WINDIR'), 'explorer.exe')
    subprocess.run([FILEBROWSER_PATH, path])


def main():
    print(Path.home())
    arguments = sys.argv[1:]

    URL = YouTube(arguments[0])
    stream = URL.streams.filter(only_audio=True)[-1]

    destination = os.path.join(Path.home(), 'Downloads\\Audio')

    print(f"Downloading {URL.title} to {destination} ...")

    os.chdir(destination)

    stream.download()

    print("Downloading completed")

    open_explorer(os.getcwd())


if __name__ == "__main__":
    main()
