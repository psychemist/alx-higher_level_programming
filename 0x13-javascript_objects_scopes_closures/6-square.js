#!/usr/bin/node

const Rhombus = require('./5-square');

module.exports = class Square extends Rhombus {
  charPrint (c) {
    let line;
    const square = [];

    if (c) {
      this.fig = c;
    } else {
      this.fig = 'X';
    }

    for (let i = 0; i < this.height; i++) {
      line = '';
      for (let j = 0; j < this.width; j++) {
        line += this.fig;
      }
      square.push(line);
    }
    console.log(square.join('\n'));
  }
};
