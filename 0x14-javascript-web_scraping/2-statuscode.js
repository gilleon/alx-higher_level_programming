#!/usr/bin/node
// displays the code of a GET request

const req = require("req");
req(process.argv[2], function (error, response) {
  console.log(error || "code:", response && response.statusCode);
});
