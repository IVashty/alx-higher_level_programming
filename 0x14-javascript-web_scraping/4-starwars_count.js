#!/usr/bin/node
// requests helps us retrieve the number of movies with character....
const request = require('request');

const SWsapi = process.argv[2];
const characterID = 18;

request(SWsapi, (error, response, body) => {
  if (error) {
    console.error(error);
    return;
  }

  if (response.statusCode !== 200) {
    console.error(response.statusCode);
    return;
  }

  const movies = JSON.parse(body).results;
  let count = 0;

  movies.forEach(movie => {
    movie.characters.forEach(character => {
      if (character.endsWith(`/${characterID}/`)) {
        count++;
      }
    });
  });

  console.log(`${count}`);
});
