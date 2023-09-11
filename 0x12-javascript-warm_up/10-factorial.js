#!/usr/bin/node

function fact (f) {
  if (isNaN(f)) {
    return 1;
  }
  if (f <= 1) {
    return 1;
  } else {
    return f * fact(f - 1);
  }
}

const arg = process.argv[2];
const num = parseInt(arg);

console.log(fact(num));
