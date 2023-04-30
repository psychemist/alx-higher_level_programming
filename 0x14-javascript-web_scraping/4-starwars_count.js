#!/usr/bin/node

const url = process.argv[2];
const request = require('request');

request(url, (err, response, body) => {
  if (!err && response.statusCode === 200) {
    const films = JSON.parse(body);
    const movies = []
    let count = 0;

    for (const film of films.results) {
      for (const xter of film.characters) {
        if (xter.includes('18')) {
          count++;
        }
      }
    }

    console.log(count);
  }
});
