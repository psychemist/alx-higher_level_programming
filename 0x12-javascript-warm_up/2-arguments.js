#!/usr/bin/node

// Include process module
const argv = require('process').argv;

// Loop over each argument and print log
if (argv.length === 2) {
  console.log('No argument');
} else if (argv.length === 3) {
  console.log('Argument found');
} else console.log('Arguments found');
