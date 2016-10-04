#! /usr/bin/env python
# -*- coding:utf-8 -*-

import sys
import os
import namedtuple

class BCHCode(object):
    """docstring for BCHCode."""
    def __init__(self, n, k, t):
        self.n = n
        self.k = k
        self.t = t

    def getErrorRate(self):
        return float(self.t)/self.n

    def getCodeRate(self):
        return float(self.k)/self.n

n = 511
k_values = []
t_values = []





def do():
  pass

def main():
  do()

if __name__ == "__main__":
  sys.exit(main())
