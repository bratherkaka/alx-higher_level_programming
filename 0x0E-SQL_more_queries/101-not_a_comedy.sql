-- This script lists all shows without the genre Comedy in the hbtn_0d_tvshows database

SELECT tv_shows.title
FROM tv_shows
WHERE tv_shows.id NOT IN
(SELECT tv_show_genres.tv_show_id
FROM tv_show_genres
JOIN tv_genres ON tv_genres.id = tv_show_genres.tv_genre_id
WHERE tv_genres.name = 'Comedy')
ORDER BY tv_shows.title ASC;

