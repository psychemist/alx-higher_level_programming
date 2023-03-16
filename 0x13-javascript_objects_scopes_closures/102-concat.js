#!/usr/bin/node

const argv = require('process').argv;
const fs = require('fs');

const str1 = fs.readFileSync(argv[2]);
const str2 = fs.readFileSync(argv[3]);
const str3 = str1 + str2;
fs.writeFileSync(argv[4], str3);
