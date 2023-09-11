#!/usr/bin/node

const a = process.argv[2];
const b = process.argv[3];

const x = parseInt(a);
const y = parseInt(b);

function add (a, b) {
  console.log(a + b);
}

add(x, y);
