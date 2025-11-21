from spotify_auth import SpotifyAuth


class PlaylistCreator:
    def __init__(self, sp_auth: SpotifyAuth):
        self.sp = sp_auth.sp
        self.user_id = sp_auth.user_id

    def create_playlist(self, name: str, description: str = ""):
        playlist = self.sp.user_playlist_create(
            user=self.user_id,
            name=name,
            public=False,
            description=description
        )
        print(playlist["external_urls"]["spotify"])
        return playlist["id"]
