#!/usr/bin/python3
# -*- coding: utf-8 -*-

'''
    2016 ICPC at UCSY
    Problem-A: Evaluating Fully Parenthesized Expression
               This version relys on Python's eval() function,
               which does not exist in many language. unfair :-)
               I will make another version that can be converted to
               other languages later
'''
import sys


class TestCase():
    pass


def solve(tc):
    '''
        Input: Test Case
        Return: None
    '''

    try:
        result = eval(sys.stdin.readline())
    except ZeroDivisionError:
        print('Infinity')
    else:
        print(float(result))
    return


##
##  Main routine
##
if __name__ == '__main__':
    tc = TestCase()
    tc.t = int(sys.stdin.readline())
    
    for i in range(tc.t):
        solve(tc)
