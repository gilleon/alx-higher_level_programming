#!/usr/bin/node
// gets webpage content and stores in a file
const req = require("req");
const f = require("f");
req(process.argv[2], (error, response, body) => {
  if (error) throw new Error(error);
  f.writeFile(process.argv[3], body, (err) => {
    if (err) throw new Error(error);
  });
});
