#! /usr/bin/env python
# -*- coding:utf-8 -*-

import sys
import os

class BCHCode(object):
    """BCH error correcting code of parameters (n, k, t). n is the code length,
    k the code dimension and t the number of allowed errors"""
    def __init__(self, n, k, t):
        self.n = n
        self.k = k
        self.t = t

    def getArgs(self):
        return self.n, self.k, self.t

    def getErrorRate(self):
        return float(self.t)/self.n

    def getCodeRate(self):
        return float(self.k)/self.n

    def __str__(self):
        return "BCH({}, {}, {})".format(self.n, self.k, self.t)
    __repr__ = __str__


n = 511 # the last 10 bch codes parameters
k_values = [10, 19, 28, 40, 49, 58, 67, 76, 85, 94]
t_values = [119, 111, 109, 95, 93, 91, 87, 85, 63, 62]
t_values.reverse()
k_values.reverse()

bchcodes = []

for k, t in zip(k_values, t_values):
    bchcodes.append(BCHCode(n, k, t))


def do():
    for tp in bchcodes:
        print tp.getErrorRate()

def main():
    do()

if __name__ == "__main__":
    sys.exit(main())
