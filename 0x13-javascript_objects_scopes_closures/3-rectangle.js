#!/usr/bin/node

class Rectangle {
  constructor(w, h) {
    if (w <= 0 || h <= 0 || typeof w !== 'number' || typeof h !== 'number') {
      return {};
	}
	this.width = w;
    this.height = h;
  }

  print() {
    for (let k = 0; k < this.height; k++) {
      let row = '';
	  for (let p = 0; p < this.width; p++) {
        row += 'X';
	  }
      console.log(row);
	}
  }
}

module.exports = Rectangle;
