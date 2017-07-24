#!/usr/bin/python3
# -*- coding: utf-8 -*-

'''
    2016 ICPC at UCSY
    Problem-?: 
'''
import sys


class TestCase():
    pass


def parse_tc(tc):
    '''
        Input: Test Case
        Update: Start Location, Delivery List
        Return: None
    '''

    tc.n = int(sys.stdin.readline())
    tc.array = list(map(int,sys.stdin.readline().split()))

    return


def solve(tc):
    '''
        Input: Test Case
        Return: None
    '''

    parse_tc(tc)

    print(total)
    return


##
##  Main routine
##
if __name__ == '__main__':
    
    tc = TestCase()
    tc.t = int(sys.stdin.readline())
    
    for i in range(tc.t):
        solve(tc)
