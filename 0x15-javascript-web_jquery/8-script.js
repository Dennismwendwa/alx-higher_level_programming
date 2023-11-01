// listing all movies from star wars

$(document).ready(function() {
  $.get('https://swapi-api.alx-tools.com/api/films/?format=json', function(data) {
    
    var movies = data.results;

    var listMovies = $('#list_movies');
    $.each(movies, function(index, movie) {
      var movieTitle = movie.title;
      listMovies.append('<li>' + movieTitle + '</li>');
    });
  });
});
