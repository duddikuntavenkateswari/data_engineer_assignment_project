DROP TABLE IF EXISTS movies;
DROP TABLE IF EXISTS ratings;

CREATE TABLE movies (
    movie_id INTEGER PRIMARY KEY,
    title TEXT,
    genre TEXT,
    director TEXT,
    year TEXT
);

CREATE TABLE ratings (
    user_id INTEGER,
    movie_id INTEGER,
    rating REAL
);
