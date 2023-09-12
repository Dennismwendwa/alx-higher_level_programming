#!/usr/bin/node

class Rectangle {
  constructor(w, h) {
	if (h <= 0 || w <= 0 || typeof w !== 'number' || typeof h !== 'number') {
    return {};
	}
    this.width = w;
    this.height = h;
  }
}

module.exports = Rectangle;
