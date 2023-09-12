#!/usr/bin/node

const lastSquare = require('./5-square');

class Square extends lastSquare {
  charPrint (c) {
    if (c === undefined) {
      c = 'X';
	}
	for (let k = 0; k < this.height; k++) {
      let row = '';
      for (let w = 0; w < this.width; w++) {
        row += c;
	  }
      console.log(row);
	}
  }
}

module.exports = Square;
