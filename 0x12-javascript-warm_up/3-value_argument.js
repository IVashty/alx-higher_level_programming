#!/usr/bin/node

// if no argument is passed print no argument
const myArgument = process.argv[2];
if (myArgument === undefined) {
  console.log('No argument');
} else {
  console.log(myArgument);
}
