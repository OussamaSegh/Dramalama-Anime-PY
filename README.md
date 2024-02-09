# Anime Search and Streaming Script

This Python script allows users to search for anime and stream episodes from the search results. It utilizes the Consumet API to fetch information about anime and episode links, and it also integrates a custom web-based video player for streaming episodes.

## Features

- Search for anime by name
- Display available anime along with release year
- View detailed information about the chosen anime
- Select and stream episodes from the chosen anime using a custom video player

## Prerequisites

- Python 3.x
- Requests library (can be installed via `pip install requests`)
- Web browser with HTML5 video support

## Custom Video Player

This script utilizes a custom web-based video player specifically designed for streaming anime episodes. The video player can be accessed via the following URL:

[Anime Streaming Video Player](https://dramalama-video-player.vercel.app/)

The video player accepts the video link as a query parameter in the URL. When streaming an episode, the script automatically opens the selected episode in the custom video player.

## Usage

1. Clone the repository or download the `main.py` file.
2. Make sure you have Python installed on your system.
3. Install the Requests library if you haven't already (`pip install requests`).
4. Run the script by executing `python main.py`.
5. Follow the prompts to search for anime, choose episodes, and stream them.

## Instructions

1. When prompted, enter the name of the anime you want to watch.
2. Select the desired anime from the search results by entering its corresponding serial number.
3. View the detailed information about the anime.
4. Choose the episode you want to watch.
5. The script will open a web browser and stream the selected episode using the custom video player.

## Credits

- Consumet API: [Consumet](https://github.com/consumet/api.consumet.org)
- Custom Video Player: [Anime Streaming Video Player](https://github.com/real-zephex/Video-Player)

## Disclaimer

This script is meant for educational purposes only. Make sure to respect the terms of service of the streaming platforms and APIs used.

