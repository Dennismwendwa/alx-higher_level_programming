#!/usr/bin/node

const fs = require('fs');
const file1 = process.argv[2];
const file2 = process.argv[3];
const file1Content = fs.readFileSync(file1);
const file2Content = fs.readFileSync(file2);

const allContent = file1Content + file2Content;

fs.writeFile(process.argv[4], allContent, 'utf-8', (errors) => {
  if (errors) {
    console.error(errors);
  }
});
