'use strict';

var BinaryIndexedTree = require('./binaryIndexedTree.js');

var tree = new BinaryIndexedTree();

var numbers = [19, 11, 15, 4, 7, 13, 11, 2];

tree.loadNumbers(numbers, 'min');

console.log(tree.bt);
