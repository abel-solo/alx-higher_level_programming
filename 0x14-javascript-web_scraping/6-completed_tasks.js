#!/usr/bin/node
const request = require('request');
const endpoint = process.argv[2]
request(endpoint, function (err, response, body) {
  if (!err) {
    const tasks = JSON.parse(body);
    const done = {};
    tasks.forEach((todo) => {
      if (todo.done && done[todo.userId] === undefined) {
        done[todo.userId] = 1;
      } else if (todo.done) {
        done[todo.userId] += 1;
      }
    });
    console.log(done);
  }
});
