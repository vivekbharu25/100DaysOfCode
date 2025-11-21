import requests
from bs4 import BeautifulSoup

response = requests.get("https://news.ycombinator.com/news")
soup = BeautifulSoup(response.text, "html.parser")

# Get all article titles + links
article_texts = soup.select(".titleline a")
print(article_texts)

titles = []
links = []
# Get first score
for texts in article_texts[::2]:
    titles.append(texts.get_text())
    links.append(texts.get("href"))

scores = [int(score.getText().split()[0]) for score in soup.select(".score")]

ind = scores.index(max(scores))

print(titles[ind])
print(links[ind])
print(scores[ind])

