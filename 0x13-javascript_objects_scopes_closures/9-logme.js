#!/usr/bin/node

let log = -1;
exports.logMe = function (item) {
  log++;
  console.log(log + ':' + item);
};
