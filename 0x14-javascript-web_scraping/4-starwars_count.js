#!/usr/bin/node
// printing the number of movies where "Wedge Antilles" is present

const request = require('request');

const apiUrl = process.argv[2];

request(apiUrl, (error, response, body) => {
  if (error) {
    console.error(error);
  } else {
    if (response.statusCode === 200) {
      const films = JSON.parse(body);
      let wedgeAntillesFilms = 0;
      for (const res of films.results) {
        for (const url of res.characters) {
          if (url.includes(18)) {
            wedgeAntillesFilms++;
          }
        }
      }
      console.log(wedgeAntillesFilms);
    }
  }
});
