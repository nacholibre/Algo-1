'use strict';

var BinaryIndexedTree = require('./binaryIndexedTree.js');
var assert = require('assert');

var tree = new BinaryIndexedTree();

//var numbers = [1, 6, 12, 3, 14, 70];
//
//tree.loadNumbers(numbers);
//
//tree.update(2, 10);
//
//console.log(tree.query(3));

var totalDates = [];

for (var i = 1; i <= 365; i++) {
    totalDates.push(0);
}

tree.loadNumbers(totalDates);

var peoplebds = [5, 10, 6, 7, 3, 4, 5, 11, 21, 300, 15];

peoplebds.forEach(function(bd) {
    tree.increase(bd, 1);
});

function queryBD(start, end) {
    var r = tree.query(end+1) - tree.query(start);
    return r;
}

assert(queryBD(2, 10) === 7);
assert(queryBD(10, 365) === 5);

tree.increase(8, 3);

assert(queryBD(7, 11) === 6);

tree.decrease(8, 2);

assert(queryBD(7, 11) === 4);

tree.increase(18, 5);

assert(queryBD(10, 20) === 8);

console.log('All tests passed YAAAAAAAAAAAY!');
