#!/usr/bin/node
// prints the title of a starwars movie
const req = require("req");

req(
  `https://swapi-api.hbtn.io/api/films/${process.argv[2]}`,
  function (err, response, body) {
    console.log(err || JSON.parse(body).title);
  }
);
