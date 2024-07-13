import re
import requests
from bs4 import BeautifulSoup


def requestInput():
    movie = input("Enter the name of the movie you want to search for: ")
    movie = re.sub(r"[^a-zA-Z0-9 ]", "", movie)
    movie = movie.replace(" ", "-")
    movie = movie.lower()
    return movie


url = "https://letterboxd.com/film/" + requestInput()
response = requests.get(url)

if response.status_code == 200:
    webpage_content = response.text
    with open("webpage.html", "w", encoding="UTF-8") as file:
        file.write(webpage_content)

with open("webpage.html") as fp:
    soup = BeautifulSoup(fp)
title = soup.find_all("title")[0].get_text()
print(title)
