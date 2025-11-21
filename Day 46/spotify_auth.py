import spotipy
from spotipy.oauth2 import SpotifyOAuth


class SpotifyAuth:
    def __init__(self):
        self.sp = spotipy.Spotify(
            auth_manager=SpotifyOAuth(
                client_id="574263d2abcf4047bdc695ae6825608e",
                client_secret="ed52d259af5442a08d7eb7c507370e6e",
                redirect_uri="http://localhost:8888/callback",  # ✅ must be localhost callback
                scope="playlist-modify-public playlist-modify-private"
            )
        )
        self.user_id = self.sp.me()["id"]  # fetch current user id
