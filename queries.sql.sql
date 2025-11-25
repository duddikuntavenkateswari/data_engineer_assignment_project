-- 1) Highest rated movie
SELECT m.title, AVG(r.rating) AS avg_rating
FROM movies m
JOIN ratings r ON m.movie_id = r.movie_id
GROUP BY m.movie_id
ORDER BY avg_rating DESC
LIMIT 1;

-- 2) All movies with avg rating
SELECT m.title, IFNULL(AVG(r.rating), 0) AS avg_rating
FROM movies m
LEFT JOIN ratings r ON m.movie_id = r.movie_id
GROUP BY m.movie_id;

-- 3) Movies without ratings
SELECT title
FROM movies
WHERE movie_id NOT IN (SELECT movie_id FROM ratings);
