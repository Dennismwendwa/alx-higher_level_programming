#!/usr/bin/node

function callMeMoby (x, theFunction) {
  for (let k = 0; k < x; k++) {
    theFunction();
  }
}

module.exports = { callMeMoby };
