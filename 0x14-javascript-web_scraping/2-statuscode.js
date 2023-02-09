#!/usr/bin/node
// using the request module of get request.
const request = require('request');

const url = process.argv[2];

request.get(url, (error, response, body) => {
  if (error) {
    console.error(error);
    return;
  }
  console.log(`code: ${response.statusCode}`);
});
