from bs4 import BeautifulSoup
import requests
import spotipy
from spotipy.oauth2 import SpotifyOAuth

SPOTIPY_CLIENT_ID = "fe6a678914a343ba9b648e2d9cc1edd7"
SPOTIPY_CLIENT_SECRET = "64e9deb02d4047c6aabc78001ffc41d6"
date = input("Which year do you want to travel to? Type the date in this format YYYY-MM-DD: ")
url = f"https://www.billboard.com/charts/hot-100/{date}"

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(
            scope="playlist-modify-private",
            redirect_uri="https://developer.spotify.com/dashboard/applications/fe6a678914a343ba9b648e2d9cc1edd7",
            client_id=SPOTIPY_CLIENT_ID,
            client_secret=SPOTIPY_CLIENT_SECRET,
            show_dialog=True,
            cache_path="token.txt")
                     )
user_id = sp.current_user()["id"]

response = requests.get(url).text

soup = BeautifulSoup(response, "html.parser")
songs = soup.find_all("span", class_="chart-element__information__song text--truncate color--primary")

song_names = [song.getText() for song in songs]



song_uris = []
year = date.split("-")[0]
for song in song_names:
    result = sp.search(q=f"track:{song} year:{year}", type="track")
    try:
        uri = result["tracks"]["items"][0]["uri"]
        song_uris.append(uri)
    except IndexError:
        print(f"{song} doesn't exist in Spotify. Skipped.")

playlist_id = f"{date}Billboard 100"
create_playlist = sp.user_playlist_create(user_id, name=playlist_id, public=False)
new_playlist = sp.user_playlist_add_tracks(user= user_id, playlist_id=create_playlist["id"],tracks=song_uris)














