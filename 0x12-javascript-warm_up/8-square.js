#!/usr/bin/node

const args = process.argv[2];
const number = parseInt(args);

if (!isNaN(number)) {
  for (let s = 0; s < number; s++) {
    let row = '';
    for (let k = 0; k < number; k++) {
      row += 'X';
    }
    console.log(row);
  }
} else {
  console.log('Missing size');
}
