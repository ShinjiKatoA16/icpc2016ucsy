#!/usr/bin/python3
# -*- coding: utf-8 -*-

'''
    2016 ICPC at UCSY
    Problem-G: Vampire Number
    Performance is not enough to solve 8 digit number. Unfortunately dumb 
    version (prob_g2.py) is faster
'''
import sys
import itertools as itr


class TestCase():
    pass


def parse_tc(tc):
    '''
        Input: Test Case
        Update: Lower boudary, Upper boundary
        Return: None
    '''

    (tc.L,tc.U) = list(map(int,sys.stdin.readline().split()))

    return


def get_fangs(n_str):
    '''
        Input: String format of Integer
        Return: Pair of Fangs, if the integer is Vampire number
                False if the number is not Vampire number
    '''
    n_list = list(itr.permutations(n_str, len(n_str)))
    for nlstr in n_list:
        s = ''.join(nlstr)
        x,y = s[:len(s)//2], s[len(s)//2:]
        if x > y:
            continue
        if x[0] == '0' or y[0] == '0':
            continue
        if x[-1] == '0' and y[-1] == '0':
            continue
        if int(x) * int(y) == int(n_str):
            return x,y
    return False


def vampire(n):
    '''
        Input: Integer
        Return: True if the integer is Vampire number
                False if the number is not Vampire number
    '''
    n_str = str(n)
    if (len(n_str) < 3) or (len(n_str) % 2 != 0):
        return False 

    fangs = get_fangs(n_str)
    if not fangs:
        return False 

    print(n, '=', fangs[0], '*', fangs[1], sep='')
    return True 



def solve(tc):
    '''
        Input: Test Case
        Return: None
    '''

    parse_tc(tc)
    total = 0
    for n in range(tc.L, tc.U+1):
        if vampire(n):
            total += 1
    if total == 0:
        print('NONE')

    return


##
##  Main routine
##
if __name__ == '__main__':
    
    tc = TestCase()
    tc.t = int(sys.stdin.readline())
    
    for i in range(tc.t):
        print('Case ', i+1, ':', sep='')
        solve(tc)
