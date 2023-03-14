#!/usr/bin/node

const arr = process.argv.slice(2);

if (arr.length < 2) {
  console.log('0');
} else {
  arr.sort((x, y) => x - y);
  arr.pop();
  console.log(arr.pop());
}
