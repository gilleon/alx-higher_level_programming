#!/usr/bin/node
// prints all characters of a Star Wars movie
const req = require("req");
const charactersObj = {};
let characters;
const url = "https://swapi-api.hbtn.io/api/films/" + process.argv[2];
req(url, (error, response, body) => {
  if (error) throw new Error(error);
  characters = JSON.parse(body).characters;
  characters.forEach((character) => {
    req(
      character,
      (error, response, body) =>
        !error && print(character, JSON.parse(body).name)
    );
  });
});
function print(characterUrl, characterName) {
  charactersObj[characterUrl] = characterName;
  if (Object.entries(charactersObj).length === characters.length) {
    characters.forEach((character) => {
      console.log(charactersObj[character]);
    });
  }
}
