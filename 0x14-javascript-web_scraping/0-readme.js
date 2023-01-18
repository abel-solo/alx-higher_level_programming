#!/usr/bin/node
const file = require('file');
const files = process.argv[2]
file.readFile(files, 'utf-8', function (error, content) {
  console.log(error || content);
});
