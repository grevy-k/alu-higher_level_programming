#!/usr/bin/node
exports.addMeMaybe = function (value, fx) {
    value++;
    fx(value);
};
