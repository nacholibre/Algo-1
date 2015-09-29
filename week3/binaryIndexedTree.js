'use strict';

function BinaryIndexedTree() {
    this.bt = [];
}

BinaryIndexedTree.prototype = {
    _findPow2ArraySize: function(arrSize) {
        var stepen = 2;

        while (arrSize > stepen) {
            stepen = stepen * 2;
        }

        return stepen;
    },
    _createEmptyArrOfSize: function(size) {
        var arr = [];

        for (var i = 0; i < size; i++) {
            arr.push(0);
        }

        return arr;
    },
    loadNumbers: function(array, type) {
        type = type || 'sum';

        var arraySizeStepen = this._findPow2ArraySize(array.length);

        array = array.concat(this._createEmptyArrOfSize(arraySizeStepen - array.length));

        var leftPart = this._createEmptyArrOfSize(arraySizeStepen);

        var bt = leftPart.concat(array);

        for (var i = (bt.length/2)-1; i > 0; i--) {
            var child1 = bt[2*i];
            var child2 = bt[(2*i) + 1];

            if (type === 'sum') {
                bt[i] = child1 + child2;
            } else if (type === 'min') {
                var min = child1;

                if (child1 > child2) {
                    min = child2;
                }

                bt[i] = min;
            }
        }

        this.bt = bt;
    },
    _updateFromLeaf: function(leafPos) {
        var parentPosition = Math.floor(leafPos/2);

        while (parentPosition > 0) {
            this.bt[parentPosition] = this.bt[2*parentPosition] + this.bt[2*parentPosition+1];
            parentPosition = Math.floor(parentPosition/2);
        }
    },
    _getLeafPos: function(pos) {
        var startIndex = this.bt.length/2-1;
        var leafPos = startIndex+pos;

        return leafPos;
    },
    update: function(pos, num) {
        var leafPos = this._getLeafPos(pos);

        this.bt[leafPos] = num;

        this._updateFromLeaf(leafPos);
    },
    increase: function(pos, incrby) {
        var leafPos = this._getLeafPos(pos);

        this.bt[leafPos] = this.bt[leafPos] + incrby;

        this._updateFromLeaf(leafPos);
    },
    decrease: function(pos, decrby) {
        var leafPos = this._getLeafPos(pos);

        this.bt[leafPos] = this.bt[leafPos] - decrby;

        this._updateFromLeaf(leafPos);
    },
    query: function(i) {
        var sum = 0;

        var startIndex = this.bt.length/2-1;

        var leafPos = startIndex+i;

        while (leafPos !== 1) {
            if (leafPos % 2 === 0) {
                //left child
                //pass
            } else {
                sum += this.bt[leafPos-1];
                //right child
            }

            leafPos = Math.floor(leafPos/2);
        }

        return sum;
    },
    queryMinRange: function(start, end) {
    },
};

module.exports = BinaryIndexedTree;

//var tree = new BinaryIndexedTree();
//
////var numbers = [1, 6, 12, 3, 14, 70];
////
////tree.loadNumbers(numbers);
////
////tree.update(2, 10);
////
////console.log(tree.query(3));
//
//var totalDates = [];
//
//for (var i = 1; i <= 365; i++) {
//    totalDates.push(0);
//}
//
//tree.loadNumbers(totalDates);
//
//var peoplebds = [5, 10, 6, 7, 3, 4, 5, 11, 21, 300, 15];
//
//peoplebds.forEach(function(bd) {
//    tree.increase(bd, 1);
//});
//
//function queryBD(start, end) {
//    var r = tree.query(end+1) - tree.query(start);
//    return r;
//}
//
//assert(queryBD(2, 10) === 7);
//assert(queryBD(10, 365) === 5);
//
//tree.increase(8, 3);
//
//assert(queryBD(7, 11) === 6);
//
//tree.decrease(8, 2);
//
//assert(queryBD(7, 11) === 4);
//
//tree.increase(18, 5);
//
//assert(queryBD(10, 20) === 8);
//
//console.log('All tests passed YAAAAAAAAAAAY!');

//function createEmptyArrOfSize(size) {
//    var arr = [];
//
//    for (var i = 0; i < size; i++) {
//        arr.push(0);
//    }
//
//    return arr;
//}
//
//function findPow2ArraySize(arrSize) {
//    var stepen = 2;
//
//    while (arrSize > stepen) {
//        stepen = stepen * 2;
//    }
//
//    return stepen;
//}
//
//function createBinaryTreeArray(array) {
//    var arraySizeStepen = findPow2ArraySize(array.length);
//
//    array = array.concat(createEmptyArrOfSize(arraySizeStepen - array.length));
//
//    var leftPart = createEmptyArrOfSize(arraySizeStepen);
//
//    return leftPart.concat(array);
//}
//
//var numbers = [1, 6, 12, 3, 14, 70];
//
//console.log('Numbers');
//console.log(numbers);
//
//var numbersSum = numbers.reduce(function(prev, current) {
//    return prev + current;
//});
//
//
//console.log('Numbers sum: ' + numbersSum);
//
//console.log(numbers.length);
//var bt = createBinaryTreeArray(numbers);
//console.log(bt);
//console.log(bt.length);
//
//console.log('====');
//for (var i = (bt.length/2)-1; i > 0; i--) {
//    var child1 = bt[2*i];
//    var child2 = bt[(2*i) + 1];
//
//    bt[i] = child1 + child2;
//}
//
//console.log(bt);
//
//function updateElement(pos, num) {
//    var startIndex = bt.length/2-1;
//
//    var leafPos = startIndex+pos;
//    console.log('left pos: ' + leafPos);
//    console.log('left value: ' + bt[leafPos]);
//
//    bt[leafPos] = num;
//
//    var parentPosition = Math.floor(leafPos/2);
//
//    while (parentPosition > 0) {
//        bt[parentPosition] = bt[2*parentPosition] + bt[2*parentPosition+1];
//        parentPosition = Math.floor(parentPosition/2);
//    }
//}
//
//updateElement(2, 6);
//
//function query(i) {
//    var sum = 0;
//
//    var startIndex = bt.length/2-1;
//
//    var leafPos = startIndex+i;
//
//    while (leafPos !== 1) {
//        if (leafPos % 2 === 0) {
//            //left child
//            //pass
//        } else {
//            sum += bt[leafPos-1];
//            //right child
//        }
//
//        leafPos = Math.floor(leafPos/2);
//    }
//
//    return sum;
//}
//
//var r = query(4);
//console.log(r);
