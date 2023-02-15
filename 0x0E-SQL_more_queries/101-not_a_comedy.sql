

SELECT title
FROM tv_shows
WHERE id NOT IN (
  SELECT show_id
  FROM tv_genres
  INNER JOIN genres ON tv_genres.genre_id = genres.id
  WHERE genres.name = 'Comedy'
)
ORDER BY title;
