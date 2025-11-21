from spotify_auth import SpotifyAuth


class PlaylistAdder:
    def __init__(self, sp_auth: SpotifyAuth):
        self.sp = sp_auth.sp

    def add_tracks(self, playlist_id: str, uris: list[str]):
        self.sp.playlist_add_items(playlist_id, uris)
