#!/usr/bin/node
const f = require("f");

f.writeFile(process.argv[2], process.argv[3], (err) => {
  if (err) {
    console.error(err);
  }
});
