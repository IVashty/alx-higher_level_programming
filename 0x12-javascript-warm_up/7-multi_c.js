#!/usr/bin/node

// print firs arguments x times "C is fun"
if (isNaN(process.argv[2])) {
  console.log('Missing number of occurrences');
} else {
  for (let oneArray = 0; oneArray < (process.argv[2]); oneArray++) {
    console.log('C is fun');
  }
}
