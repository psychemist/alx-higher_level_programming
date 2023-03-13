#!/usr/bin/node

// Include process module
const process = require('process');

// Loop over each argument and print log
let count = 0;

process.argv.forEach(() => {
  count += 1;
});

if (count === 2) {
  console.log('No argument');
} else console.log(process.argv[2]);
