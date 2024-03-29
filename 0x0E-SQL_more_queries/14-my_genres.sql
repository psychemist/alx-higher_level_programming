-- lists all genres of the show Dexter from the hbtn_0d_tvshows database

SELECT name
  FROM tv_genres
  JOIN tv_show_genres
    ON tv_genres.id = tv_show_genres.genre_id
  JOIN tv_shows
    ON tv_shows.id = tv_show_genres.show_id
 WHERE title = "Dexter"
 ORDER BY name ASC;
