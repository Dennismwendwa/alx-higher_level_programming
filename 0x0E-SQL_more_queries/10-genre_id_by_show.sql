-- list all shows
SELECT tv_shows.title, tv_show_genres.genre_id FROM tv_shows JOIN
tv_shows_genres ON tv_show.id = tv_show_genres.show_id WHERE
tv_show_genres.genre_id >= 1 ORDER BY tv_shows.title, tv_show_genre_id ASC;
