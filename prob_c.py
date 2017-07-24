#!/usr/bin/python3
# -*- coding: utf-8 -*-

'''
    2016 ICPC at UCSY
    Problem-C: Finding the Determinant
'''
import sys


class TestCase():
    pass


def parse_tc(tc):
    '''
        Input: Test Case
        Update: save 2 integer in the test case to tc.m and tc.n
        Return: None
    '''

    (tc.n, tc.m) = map(int, sys.stdin.readline().split())

    return


def determinant(n, m):
    '''
        n: Integer
        m: Integer
        Return: Calculated result using recursive call
    '''

    assert n > 0, 'Unexpected input'

    if n == 1: return m
    elif n == 2: return m*m - 1
    else: return (m*determinant(n-1, m) - determinant(n-2, m))


##
##  Main routine
##
if __name__ == '__main__':
    tc = TestCase()
    while True:
        parse_tc(tc)
        if (tc.n == 0 and tc.m == 0):
            break
    
        print(determinant(tc.n, tc.m))
