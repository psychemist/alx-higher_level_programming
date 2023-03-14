#!/usr/bin/node

const process = require('process');
const argv = process.argv;

if (argv.length > 3) {
  let i = 2;
  let j = 0;
  const arr = [];

  while (argv[i]) {
    arr[j] = parseInt(argv[i]);
    i++; j++;
  }

  const len = arr.length;
  const sorted = arr.sort();
  console.log(sorted[len - 2]);
} else console.log(0);
