import requests
from bs4 import BeautifulSoup

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

# Write your code below this line 👇
response = requests.get("https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/")
movies_page = response.text

soup = BeautifulSoup(movies_page, "html.parser")
titles = soup.find_all(name="h3", class_="title")
top_movies = [movie.get_text() for movie in titles]
# for movie in titles:
#     separated = movie.get_text().split(" ")[1:]
#     stripped_title = " ".join(separated)
#     top_movies.append(stripped_title)
#     with open("movies.txt", 'w') as file:
top_movies.reverse()

with open("movies.txt", 'a', encoding="utf-8") as file:
    for x in top_movies:
        file.write(x + "\n")

