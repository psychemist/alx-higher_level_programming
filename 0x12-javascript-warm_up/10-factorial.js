#!/usr/bin/node

const process = require('process');
const argv = process.argv;

function factorial (num) {
  if (num <= 1) return 1;

  return num * factorial(num - 1);
}

if (argv.length === 3) {
  console.log(factorial(argv[2]));
} else console.log(1);
