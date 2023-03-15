#!/usr/bin/node

exports.nbOccurences = function (list, searchElement) {
  let num = 0;

  for (const elem of list) {
    if (elem === searchElement) num += 1;
  }

  return num;
};
