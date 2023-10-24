#!/usr/bin/node
// printing the number of movies where "Wedge Antilles" is present

const request = require('request');

const apiUrl = process.argv[2];

request(apiUrl, (error, response, body) => {
  if (error) {
    console.error(error);
  } else {
    if (response.statusCode === 200) {
      const films = JSON.parse(body).results;
      const wedgeAntillesFilms = films.filter((film) =>
        film.characters.includes('https://swapi-api.alx-tools.com/api/people/18/')
      );
      console.log(wedgeAntillesFilms.length);
    }
  }
});
