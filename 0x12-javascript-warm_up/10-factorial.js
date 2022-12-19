#!/usr/bin/node

// factorial == (number!)
function factorial (number) {
  if (isNaN(number) || number < 2) {
    return 1;
  } else {
    return (number * factorial(number - 1));
  }
}
console.log(factorial(process.argv[2]));
