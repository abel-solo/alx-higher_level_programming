#!/usr/bin/node
const request = require('request');
const idp = process.argv[2]
const url = 'https://swapi-api.alx-tools.com/api/films/' + idp;
request(url, function (err, response, content) {
  if (!err) {
    const characters = JSON.parse(content).characters;
    characters.forEach((character) => {
      request(character, function (err, response, content) {
        if (!err) {
          console.log(JSON.parse(content).name);
        }
      });
    });
  }
});
