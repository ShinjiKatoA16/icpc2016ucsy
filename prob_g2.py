#!/usr/bin/python3
# -*- coding: utf-8 -*-

'''
    2016 ICPC at UCSY
    Problem-G: Vampire Number
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


def check_combination(n_str, x, y):
    x_str = str(x)
    y_str = str(y)
    divider_list = list(x_str+y_str)
    divider_list.sort()
    n_list = list(n_str)
    n_list.sort()
    if divider_list == n_list:
        return True
    else:
        return False



def vampire(n):
    n_str = str(n)
    if (len(n_str) < 3) or (len(n_str) % 2 != 0):
        return False 

    low_limit = 10**(len(n_str) // 2 - 1)
    high_limit_x = int(n ** 0.5)
    high_limit_y = 10**(len(n_str) // 2)

    for x in range(low_limit, high_limit_x+1):
        if n % x != 0: continue
        y = n // x
        if (y >= high_limit_y): continue
        if (x % 10 == 0) and (y % 10 == 0): continue
        if not check_combination(n_str, x, y): continue
        print(n,'=',x,'*',y,sep='')
        return True

    return False



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
