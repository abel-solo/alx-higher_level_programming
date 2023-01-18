#!/usr/bin/node
const url = process.argv[2];
const request = require('request');

request(url, function (err, response, body) {
  if (err) console.log(err);
  let count = [];
  for (const film of JSON.parse(body).results) {
    count = count.concat(film.characters);
  }
  const diff = count.filter(x => x.includes('18'));
  console.log(diff.length);
});
