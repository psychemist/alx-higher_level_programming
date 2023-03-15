#!/usr/bin/node

exports.esrever = function (list) {
  const revArr = [];
  let len = list.length;
  let i = 0;

  while (len--) {
    revArr[i] = list[len];
    i++;
  }

  return revArr;
};
