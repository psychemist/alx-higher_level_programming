-- lists all shows without the genre Comedy in the database hbtn_0d_tvshows

SELECT title 
  FROM tv_shows
 WHERE title NOT IN
       (SELECT title
          FROM tv_shows
          JOIN tv_show_genres
            ON tv_shows.id = tv_show_genres.show_id
          JOIN tv_genres
            ON tv_genres.id = tv_show_genres.genre_id
         WHERE name = "Comedy")
         ORDER BY title ASC;
