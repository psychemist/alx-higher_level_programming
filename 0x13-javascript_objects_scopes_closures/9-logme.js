#!/usr/bin/node

exports.logMe = function (item) {
  this.log = 0;

  console.log(`${this.log} : ${item}`);
  this.log++;
}
