#!/usr/bin/node

const argv = require('process').argv;
const request = require('request');
const url = argv[2];

request(url, (err, response, body) => {
  if (!err && response.statusCode === 200) {
    const todos = JSON.parse(body);
    const tasks = {};

    for (const todo of todos) {
      const id = todo.userId;

      if (todo.completed === true) {
        if (tasks[id]) {
          tasks[id] += 1;
        } else {
          tasks[id] = 1;
        }
      }
    }

    console.log(tasks);
  }
});
