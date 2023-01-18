#!/usr/bin/node
let request = require('request');
const pid = process.argv[2];
const url = 'http://swapi.co/api/films/' + pid;
request(url, function (err, httpResponse, body) {
  console.log(JSON.parse(body).title || err);
});
