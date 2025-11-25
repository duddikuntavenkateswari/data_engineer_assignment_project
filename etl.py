import pandas as pd
import requests
import sqlite3
import time

API_KEY = "14e199c0"   


def fetch_omdb_details(title):
    url = f"http://www.omdbapi.com/?t={title}&apikey={API_KEY}"

    try:
        response = requests.get(url)
        data = response.json()

        if data["Response"] == "False":
            return "", "", ""

        return (
            data.get("Genre", ""),
            data.get("Director", ""),
            data.get("Year", "")
        )

    except:
        return "", "", ""


def run_etl():
    movies = pd.read_csv("movies.csv")
    ratings = pd.read_csv("ratings.csv")

    conn = sqlite3.connect("movies.db")
    cur = conn.cursor()

    # Load schema file
    with open("schema.sql", "r") as f:
        cur.executescript(f.read())

    # Insert movie data
    for _, row in movies.iterrows():
        movie_id = row["movieId"]
        title = row["title"]

        genre, director, year = fetch_omdb_details(title)
        time.sleep(1)

        cur.execute(
            "INSERT INTO movies (movie_id, title, genre, director, year) VALUES (?, ?, ?, ?, ?)",
            (movie_id, title, genre, director, year)
        )

    # Insert ratings
    for _, row in ratings.iterrows():
        cur.execute(
            "INSERT INTO ratings (user_id, movie_id, rating) VALUES (?, ?, ?)",
            (row["userId"], row["movieId"], row["rating"])
        )

    conn.commit()
    conn.close()
    print("ETL Completed! movies.db created.")


if __name__ == "__main__":
    run_etl()
