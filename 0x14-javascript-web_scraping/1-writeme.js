#!/usr/bin/node
// using fs module to write a string to a filePath
const fs = require('fs');

const filePath = process.argv[2];
const stringToWrite = process.argv[3];

fs.appendFile(filePath, stringToWrite, 'utf-8', (error) => {
  if (error) {
    console.error(error);
  }
});
