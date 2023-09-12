#!/usr/bin/node

const { dict } = require('./101-data');

const newDict = {};

for (const key in dict) {
  const occur = dict[key];
  if (!newDict[occur]) {
    newDict[occur] = [];
  }
  newDict[occur].push(key);
}

console.log(newDict);
