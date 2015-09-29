'use strict';

function createEmptyMatrix(size) {
    size = size - 1;

    var matrix = [];

    for (var i = 0; i <= size; i++) {
        matrix[i] = [];

        for (var k = 0; k <= size; k++) {
            matrix[i][k] = 0;
        }
    }

    return matrix;
}

function getEdges(list) {
    var edges = [];

    for (var i = 0; i <= list.length; i++) {
        if (list[i] === 1) {
            edges.push(i);
        }
    }

    return edges;
}

function BFS(G, startingPoint) {
    var q = [];

    var start = startingPoint;
    q.push(start);

    var discovered = new Map();

    discovered.set(start, true);

    var path = [];

    while (q.length > 0) {
        var r = q.splice(0, 1)[0];

        path.push(r);

        if (coffeeShops.get(r)) {
            console.log(path);
            return r;
        }

        console.log(r);
        var edges = getEdges(G[r]);
        console.log(edges);
        console.log('===========');

        edges.forEach(function(edge) {
            if (!discovered.get(edge)) {
                q.push(edge);
                discovered.set(edge, true);
            }
        });
    }


    return -1;
}

var coffeeShops = new Map();
coffeeShops.set(2, true);
coffeeShops.set(5, true);
//coffeeShops.set(4, true);

var matrix = createEmptyMatrix(6);

matrix[0][1] = 1;
matrix[0][3] = 1;

matrix[1][0] = 1;
matrix[1][2] = 1;

matrix[2][1] = 1;
matrix[2][4] = 1;

matrix[3][0] = 1;

matrix[4][2] = 1;
matrix[4][5] = 1;

matrix[5][4] = 1;

console.log(matrix);

var r = BFS(matrix, 0);

console.log('path');
console.log(r);

console.log('closest: ' + r);
