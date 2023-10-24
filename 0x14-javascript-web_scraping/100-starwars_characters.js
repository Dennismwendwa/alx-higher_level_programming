#!/usr/bin/node
// this script prints all characters of a movie

const request = require('request');

const movieId = process.argv[2];
const apiUrl = `https://swapi-api.alx-tools.com/api/films/${movieId}/`;

request(apiUrl, (error, response, body) => {
  if (error) {
    console.error(error);
  } else {
    if (response.statusCode === 200) {
      const movie = JSON.parse(body);
      const characterUrls = movie.characters;

      characterUrls.forEach((characterUrl) => {
        request(characterUrl, (charError, charResponse, charBody) => {
          if (!charError && charResponse.statusCode === 200) {
            const character = JSON.parse(charBody);
            console.log(character.name);
          }
        });
      });
    }
  }
});
