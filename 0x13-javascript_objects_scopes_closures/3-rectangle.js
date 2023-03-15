#!/usr/bin/node

module.exports = class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    let line;
    const square = [];

    for (let i = 0; i < this.height; i++) {
      line = '';
      for (let j = 0; j < this.width; j++) {
        line += 'X';
      }
      square.push(line);
    }
    console.log(square.join('\n'));
  }
};
