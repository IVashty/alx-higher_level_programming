#!/usr/bin/node

// prints a number and changes it to an  integer value
if (isNaN(process.argv[2])) {
  console.log('Not a number');
} else {
  console.log('My number: ' + process.argv[2]);
}
