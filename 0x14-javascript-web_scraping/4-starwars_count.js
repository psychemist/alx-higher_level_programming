#!/usr/bin/node

const url = process.argv[2];
const antilles = 'https://swapi-api.alx-tools.com/api/people/18/';
const request = require('request');

request(url, (err, response, body) => {
  if (!err && response.statusCode === 200) {
    const films = JSON.parse(body);
    let wedge = 0;

    for (const film of films.results) {
      for (const xter of film.characters) {
        if (xter === antilles) {
          wedge++;
        }
      }
    }

    console.log(wedge);
  }
});
