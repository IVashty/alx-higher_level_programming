#!/usr/bin/node
// fs module to read the content of a file.
const fs = require('fs');
const [filePath] = process.argv.slice(2);

fs.readFile(filePath, 'utf8', (err, data) => {
  if (err) {
    console.error(err);
    return;
  }
  console.log(data);
});
