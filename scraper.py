import requests
import re
from bs4 import BeautifulSoup

def requestInput():
    movie = input("Enter the name of the movie you want to search for: ")
    movie = re.sub(r'[^a-zA-Z0-9 ]', '', movie)
    movie = movie.replace(" ", "-")
    movie = movie.lower()
    return movie
movie = requestInput()

def requestInput2(movie):
    multiple = input("Are there multiple movies with this name? (y/n)")
    response = None
    if multiple == "y":
       multipleyear = input("What year was the movie released?")
       multipleyear = re.sub(r"[^0-9]", '', multipleyear)
       url = "https://letterboxd.com/film/" + movie + "-" + multipleyear
       response = requests.get(url)                      
       print(response.status_code) 
       
    if multiple == "n":    
       url = "https://letterboxd.com/film/" + requestInput()
       response = requests.get(url)
       print(response.status_code) 
       
    if response.status_code == 200:
       webpage_content = response.text
       with open("webpage.html", "w", encoding="UTF-8") as file:
        file.write(webpage_content)
requestInput2(movie)
         
          

with open("webpage.html") as fp:
    soup = BeautifulSoup(fp)
title = soup.find_all("title")[0].get_text()
print(title)
