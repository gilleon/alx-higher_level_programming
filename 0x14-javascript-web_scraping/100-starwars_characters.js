#!/usr/bin/node
// prints all characters of a Star Wars movie
const req = require("req");
const request2 = require("req");
const url = "https://swapi-api.hbtn.io/api/films/" + process.argv[2];
req(url, (error, response, body) => {
  if (error) throw new Error(error);
  JSON.parse(body).characters.forEach((character) => {
    request2(character, (error, response, body) => {
      if (error) throw new Error(error);
      console.log(JSON.parse(body).name);
    });
  });
});
