import requests
from bs4 import BeautifulSoup
from spotify_auth import SpotifyAuth
from playlist_create import PlaylistCreator
from playlist_add import PlaylistAdder


class BillboardScraper:
    def __init__(self, date: str):
        self.date = date
        self.url = f"https://www.billboard.com/charts/hot-100/{date}"
        self.headers = {
            "User-Agent": (
                "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                "AppleWebKit/537.36 (KHTML, like Gecko) "
                "Chrome/140.0.0.0 Safari/537.36 Edg/140.0.0.0"
            )
        }

    def scrape(self):
        response = requests.get(self.url, headers=self.headers)
        soup = BeautifulSoup(response.text, "html.parser")

        songs = []
        for li in soup.select("li.o-chart-results-list__item"):
            title_tag = li.select_one("h3#title-of-a-story")
            artist_tag = li.select_one("span.c-label a")

            if title_tag and artist_tag:
                title = title_tag.get_text(strip=True)
                artist = artist_tag.get_text(strip=True)
                songs.append(f"{title} {artist}")
        return songs


def main():
    date = input("Which date do you want to travel to? (YYYY-MM-DD): ")
    scraper = BillboardScraper(date)
    songs = scraper.scrape()

    # Authenticate with Spotify
    sp_auth = SpotifyAuth()
    playlist_creator = PlaylistCreator(sp_auth)
    playlist_adder = PlaylistAdder(sp_auth)

    # Create playlist
    playlist_id = playlist_creator.create_playlist(
        name=f"Billboard Hot 100 - {date}",
        description=f"Billboard Hot 100 from {date}"
    )

    # Search and add tracks
    uris = []
    for song in songs:
        result = sp_auth.sp.search(q=song, type="track", limit=1)
        tracks = result.get("tracks", {}).get("items", [])
        if tracks:
            uris.append(tracks[0]["uri"])

    # Add tracks in chunks of 100 (Spotify API limit)
    for i in range(0, len(uris), 100):
        playlist_adder.add_tracks(playlist_id, uris[i:i+100])

    print(f"Playlist created with {len(uris)} songs!")


if __name__ == "__main__":
    main()
