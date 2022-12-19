#!/usr/bin/node
const noOfArguments = process.argv.length - 2;
if (noOfArguments === 0) {
  console.log('No argument');
} else if (noOfArguments === 1) {
  console.log('Argument found');
} else {
  console.log('Arguments found');
}
