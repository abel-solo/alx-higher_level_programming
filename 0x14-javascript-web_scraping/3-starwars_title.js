#!/usr/bin/node
const request = require('request');
const pid = process.argv[2];
const url = 'https://swapi-api.hbtn.io/api/films/' + pid;
request(url, function (err, httpResponse, body) {
  console.log(JSON.parse(body).title || err);
});
