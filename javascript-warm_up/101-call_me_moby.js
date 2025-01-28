#!/usr/bin/node
exports.callMeMoby = function (n, mob) {
    for (let i = 0; i < n; i++) {
        mob();
    }
};
