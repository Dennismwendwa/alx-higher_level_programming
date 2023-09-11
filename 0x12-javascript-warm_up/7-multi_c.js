#!/usr/bin/node

const args = process.argv[2];
const number = parseInt(args);

if (!isNaN(number)) {
  for (let s = 0; s < number; s++) {
    console.log('C is fun');
  }
} else {
  console.log('Missing number of occurrences');
}
