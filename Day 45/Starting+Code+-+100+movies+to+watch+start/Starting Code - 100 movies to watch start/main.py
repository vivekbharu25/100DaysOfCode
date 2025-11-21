import requests
from bs4 import BeautifulSoup

URL = "https://www.empireonline.com/movies/features/best-movies-2/"

# Write your code below this line 👇

response = requests.get(URL)
soup = BeautifulSoup(response.text, "html.parser")

movie_titles = soup.select("h2 strong")
print(movie_titles[1].get_text().split(")", 1)[1].strip())

with open("./100_Movies.txt", "w") as file:
    for titles in reversed(movie_titles):
        file.write(titles.get_text() + "\n")