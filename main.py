from bs4 import BeautifulSoup
import requests
import spotipy
from spotipy.oauth2 import SpotifyOAuth

user_id = "burhansaydin@gmail.com"
SPOTIPY_CLIENT_ID = "fe6a678914a343ba9b648e2d9cc1edd7"
SPOTIPY_CLIENT_SECRET = "64e9deb02d4047c6aabc78001ffc41d6"
url = "https://www.billboard.com/charts/hot-100/2000-08-12"
REDIRECT_URI =f"https://api.spotify.com/v1/users/{user_id}/playlists"

header = {
    "Authorization": "playlist-modify-public",
    "Content-Type" : "application/json",
    "name" : "new"

}

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id = SPOTIPY_CLIENT_ID,
                                               client_secret=SPOTIPY_CLIENT_SECRET,
                                               redirect_uri=REDIRECT_URI,
                                               header=header))


response = requests.get(url).text

soup = BeautifulSoup(response, "html.parser")
song = soup.find_all("span", class_="chart-element__information__song text--truncate color--primary")

songs = [song.getText() for song in song]

print(songs)

#entry = input("Which year do you want to travel to? Type the date in this format. YYYY-MM-DD\n")



