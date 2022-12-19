#!/usr/bin/node

// print 3 lines bt using an arrayof string and a loop.
const array = ['C is fun', 'Python is cool', 'JavaScript is amazing'];
while (typeof (array[0]) !== 'undefined') {
  console.log(array.shift());
}
