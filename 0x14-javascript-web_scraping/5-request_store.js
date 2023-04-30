#!/usr/bin/node

const fs = require('fs');
const argv = require('process').argv;
const request = require('request');

const url = argv[2];
const file = argv[3];

request(url, (err, response, body) => {
  if (!err && response.statusCode === 200) {
    fs.writeFile(file, body, 'utf8', (err) => {
      if (err) console.log(err);
    });
  }
});
