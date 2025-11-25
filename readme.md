# Breif overview of our solution.

# Project:Build a small data pipeline that:

1)Reads movie data from CSV files ( ex: movies.csv, ratings.csv)
2)Fetches extra movie details from the OMDb API
3)Cleans and transforms the data
4)Loads everything into a SQLite database
5)Runs a few SQL queries for anal     ysis

**      Step 1: Setup Environment**

# Install Python libraries:
pip install pandas sqlalchemy requests

# Choose a database
We are using SQLite (it’s lightweight and built into Python).
A new file named movies.db will be created automatically.

# Step 2: Get the Data**

Download MovieLens “latest small” dataset in the given below link:
https://grouplens.org/datasets/movielens/latest/

You only need:
1.movies.csv
2.ratings.csv
Place both files in the same folder as your Python script.

# Step 3: Get Your OMDb API Key

1.Go to https://www.omdbapi.com/apikey.aspx
2.Choose Free Plan
3.Enter your email and get your API key (example: 8f1a2b3c)
Open etl.py and replace:
ex:OMDB_API_KEY = "8f1a2b3c"

# Step 4: Run the ETL Script

Run the Python script to perform the ETL (Extract, Transform, Load):
run the etl.py in the below syntax:
  python etl.py

# Extract
Read data from movies.csv and ratings.csv
Fetch details (Director, Plot, BoxOffice, Year) from the OMDb API

# Transform
Clean missing values
Fix data types
Create new fields (like decade)

# Load
Create database tables (movies, ratings, genres, movie_genres)
Insert cleaned and enriched data into movies.db

After it runs the program and see the output in console.
ETL finished. Data written to movies.db

# Step 5: Run Analytical Queries

Open the database:
 sqlite3 movies.db
Then written the SQL queries from queries.sql and run it see the out put.

# Step 6: Example Outputs

Ex: results will  based on dataset:

Query 1: Movie with the highest average rating
O/P:“The Shawshank Redemption” — 4.6 

Query 2: Top 5 genres with highest average rating	
O/P:Drama, Adventure, Animation, Comedy, Action

Query 3: Director with the most movies
O/P:Steven Spielberg

Query 4:Average rating of movies released each year 	
O/P:1995 → 3.7, 2000 → 3.8, 2010 → 4.0

# Design Choices

+ Used SQLite for simplicity (no setup required)

+ Used Pandas for easy CSV handling

+ Used SQLAlchemy for database connection

+ Handled missing OMDb results safely

+ Added decade column for extra insights

movie-data-pipeline/
├── etl.py          # Main Python script for Extract, Transform, Load
├── schema.sql      # SQL script to create database tables
├── queries.sql     # SQL queries for analysis
├── movies.csv      # Input movie data (from MovieLens)
├── ratings.csv     # Input rating data (from MovieLens)
└── README.md       # Project in my words (this file)


# Challenges & How I Solved Them
Challenge 1:Some movie titles didn’t match OMDb API	
Solution:Used cleaned titles and optional year filters

Challenge 2:Duplicate inserts	
Solution:Made the ETL script idempotent (safe to re-run)

Challenge 3:Missing BoxOffice/Director info	
Solution:Handled with None values instead of breaking

Challenge 4:Genre splitting	
Solution:Stored genres in a separate table (movie_genres)