#!/usr/bin/node
const fs = require('fs');
const files = process.argv[2]

fs.readFile(files, 'utf-8', function (error, content) {
  console.log(error || content);
});
