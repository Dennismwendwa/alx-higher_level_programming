#!/usr/bin/node
// order matters

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

      function fetchCharacterNames (index) {
        if (index < characterUrls.length) {
          const characterUrl = characterUrls[index];
          request(characterUrl, (charError, charResponse, charBody) => {
            if (!charError && charResponse.statusCode === 200) {
              const character = JSON.parse(charBody);
              console.log(character.name);
              fetchCharacterNames(index + 1);
            } else {
              fetchCharacterNames(index + 1);
            }
          });
        }
      }
      fetchCharacterNames(0);
    }
  }
});
