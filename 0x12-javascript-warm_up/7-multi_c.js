#!/usr/bin/node

const argv = require('process').argv;

if (Number.isInteger(Number(argv[2]))) {
  for (let i = 0; i < parseInt(argv[2]); i++) {
    console.log('C is fun');
  }
} else console.log('Missing number of occurrences');
