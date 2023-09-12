#!/usr/bin/node

exports.esrever = function (list) {
  const newlist = [];
  for (let k = list.length - 1; k >= 0; k--) {
    newlist.push(list[k]);
  }
  return newlist;
};
