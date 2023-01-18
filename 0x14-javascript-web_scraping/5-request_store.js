#!/usr/bin/node

const fs = require('fs');
const request = require('request');
const endpt = process.argv[2]
const file = process.argv[3]

request(endpt).pipe(fs.createWriteStream(file));
