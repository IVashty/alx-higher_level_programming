#!/usr/bin/node
// request module is used to GET ...
const request = require('request');

const movieID = process.argv[2];
const url = `https://swapi-api.alx-tools.com/api/films/${movieID}`;

request(url, (error, response, body) => {
  if (error) {
    console.error(`${error}`);
    return;
  }

  if (response.statusCode !== 200) {
    console.error(`${response.statusCode}`);
    return;
  }

  const data = JSON.parse(body);
  console.log(`${data.title}`);
});
