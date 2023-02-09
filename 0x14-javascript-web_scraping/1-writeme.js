#!/usr/bin/env node
// using fs module to write a string to a filePath
const fs = require('fs');

const filePath = process.argv[2];
const stringToWrite = process.argv[3];

fs.writeFile(filePath, stringToWrite, 'utf-8', (error) => {
  if (error) {
    console.error(error);
    return;
  }
  console.log(`The file was written successfully at ${filePath}`);
});
