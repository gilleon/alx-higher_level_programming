#!/usr/bin/node

let numArgPrint = 0;
exports.logMe = function (item) {
  console.log(`${numArgPrint}: ${item}`);
  numArgPrint += 1;
};
