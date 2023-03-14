#!/usr/bin/node

const argv = require('process').argv;

if (Number.isInteger(Number(argv[2]))) {
  const size = parseInt(argv[2]);
  const square = [];
  let line;

  if (size >= 1) {
    for (let i = 0; i < size; i++) {
      line = '';
      for (let j = 0; j < size; j++) {
        line += 'X';
      }
      square.push(line);
    }
    console.log(square.join('\n'));
  }
} else console.log('Missing size');
