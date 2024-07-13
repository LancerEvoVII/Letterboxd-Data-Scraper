import requests
from bs4 import BeautifulSoup
url = "https://letterboxd.com/film/all-about-lily-chou-chou" # Replace with the URL of the website you want to scrape
response = requests.get(url)

if response.status_code == 200:
  webpage_content = response.text
  with open ("webpage.html", "w", encoding= "UTF-8") as file:
    file.write(webpage_content)

with open("webpage.html") as fp:
    soup = BeautifulSoup(fp)
title = soup.find_all("title")
print(title)
