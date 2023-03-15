#!/usr/bin/node

const dict = require('./101-data.js').dict;
const dict2 = {};

for (const key in dict) {
  const val = dict[key];
  if (!dict2[val]) dict2[val] = [];
  dict2[val].push(key);
}
console.log(dict2);
