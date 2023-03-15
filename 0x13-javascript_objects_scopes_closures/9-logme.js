#!/usr/bin/node

log = 0;
exports.logMe = function (item) {
  console.log(`${log++} : ${item}`);
}
