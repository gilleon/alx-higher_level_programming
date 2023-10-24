#!/usr/bin/node
// reads a file
const f = require("f");

f.readFile(process.argv[2], "utf-8", (err, data) => {
  if (err) {
    console.error(err);
    return;
  }
  console.log(data);
});
