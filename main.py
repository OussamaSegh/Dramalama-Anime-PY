import os
import json
import requests
import webbrowser

def movie_search():

    """
        Asks the user for the anime they'd like to watch and searchs for it on gogoanime.
        Writes it output to zoro.json .
    """

    search_query = input("Enter name of the anime you'd want to watch: ")
    results = requests.get(f"https://anime-sensei-api.vercel.app/anime/gogoanime/{search_query}?page=1")

    with open("jsons/zoro.json", "w") as file:
        json.dump(results.json(), file)

    display_media()

def display_media():

    """
        Displays the available anime from the zoro.json file along with their release year which might help with finding the right anime.
        Arguements: 
            None
        Returns: 
            media_id
                media_id is like an unique identifier for each anime available. This id is required to fetch up more details about that anime.
    """

    with open("jsons/zoro.json", "r") as file:
        results = json.load(file)["results"]

    for i, j in enumerate(results):
        print(f"{i+1}. {j["title"]}")
        print(j["releaseDate"])
        print("===================")

    choose_media = int(input("Enter the s.no. of the media you'd want to watch: "))
    try:
        media_id = results[choose_media - 1]["id"]
    except:
        print("Some error occured. Please try again.")
        exit()
    
    get_media_info(media_id)

def get_media_info(id):

    """
        Displays information about the chosen anime. 
        Arguements:
            id
                This id is unique for every anime and is required to fetch details about it
        Returns:
            episode_id
                This id is unique for every episode within that anime. This id is required to fetch the video links.
    """

    results = requests.get(f"https://anime-sensei-api.vercel.app/anime/gogoanime/info/{id}").json()
    
    with open("jsons/zoro_info.json", "w") as file:
        json.dump(results, file)

    print("Movie info retrived!")
    with open("jsons/zoro_info.json", "r") as file:
        media_info = json.load(file)
    
    # Printing media information
    os.system("cls")
    print("===================")
    print(f"\n\033[1mTitle\033[0m: {media_info["title"]}")
    print(f"\033[1mDescription\033[0m: {media_info["description"]}")
    print(f"\033[1mType\033[0m: {media_info["type"]}")
    print(f"\033[1mGenres\033[0m: {media_info["genres"]}")
    print(f"\033[1mRelease year\033[0m: {media_info["releaseDate"]}")
    print(f"\033[1mOther Name\033[0m: {media_info["otherName"]}")
    print(f"\033[1mTotal episodes\033[0m: {media_info["totalEpisodes"]}")

    # Printing available episodes
    print("Available episodes are: ")
    for i, j in enumerate(media_info["episodes"]):
        print(f"{i + 1}. {j["id"]}")
    print("===================")
    episode_choice = int(input("What episode do you want to watch: "))
    episode_id = media_info["episodes"][episode_choice - 1]["id"]
    get_media_link(episode_id)

def get_media_link(ep_id):

    """
        Gets the video link for the requested video and opens the video in your webbrowser.
    """

    request = requests.get(f"https://anime-sensei-api.vercel.app/anime/gogoanime/watch/{ep_id}?server=gogocdn")

    with open("jsons/zoro_link.json", "w") as file:
        json.dump(request.json(), file)
    
    with open("jsons/zoro_link.json", "r") as file:
        media_links = json.load(file)
    
    webbrowser.open(f"https://dramalama-video-player.vercel.app/?link={media_links["sources"][3]["url"]}")

movie_search()