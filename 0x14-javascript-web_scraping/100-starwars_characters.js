#!/usr/bin/node

const id = process.argv[2];
const url = `https://swapi-api.alx-tools.com/api/films/${id}`;
const request = require('request');

request(url, (err, response, body) => {
  if (!err && response.statusCode === 200) {
    const characters = JSON.parse(body).characters;

    for (const xter of characters) {
      request(xter, (err, response, body) => {
        if (!err && response.statusCode === 200) {
          console.log(JSON.parse(body).name);
        }
      });
    }
  }
});
