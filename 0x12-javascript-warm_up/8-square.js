#!/usr/bin/node

// print firs arguments x and that prints a square
if (isNaN(process.argv[2])) {
  console.log('Missing size');
} else {
  for (let oneArray = 0; oneArray < (process.argv[2]); oneArray++) {
    console.log('X'.repeat(process.argv[2]));
  }
}
