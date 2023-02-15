-- List tv shows and their genres
-- lists all genres from hbtn_0d_tvshows and displays the number of shows linked to each.
SELECT tv_genres.name AS name
FROM tv_genres
JOIN tv_show_genres
ON tv_show_genres.genre_id = tv_genres.id
JOIN tv_shows
ON tv_shows.id = tv_show_genres.show_id
WHERE tv_shows.title='Dexter'
GROUP BY tv_genres.name;
