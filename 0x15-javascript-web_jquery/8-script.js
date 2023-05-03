$.getJSON('https://swapi-api.alx-tools.com/api/films/?format=json',
  function (movies) {
    $.each(movies.results, function (i, movie) {
      $('ul#list_movies').append('<li>' + movie.title + '</li>');
    });
  });
