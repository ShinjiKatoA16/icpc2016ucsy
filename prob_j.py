#!/usr/bin/python3
# -*- coding: utf-8 -*-

'''
    2016 ICPC at UCSY
    Problem-J: Green Frog and Ordering
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

    if tc.n != len(tc.array):
        print('parse_tc: test case number mismatch:', tc.n, len(tc.array))
        raise ValueError


    return

def is_sorted(list_x, min_value):
    if len(list_x) == 0:
        return True

    v1 = list_x[0]
    if v1 <= min_value:
        return False

    for i in range(1,len(list_x)):
        v2 = list_x[i]
        if v2 <= v1:
            return False
        v1 = v2
    else:
        return True

def solve(tc):
    '''
        Input: Test Case
        Return: None
    '''

    move_count = 0

    print('Case ', tc.t, ': ', sep='', end='')
    parse_tc(tc)

    old_list = tc.array[:]
    new_list = list()
    new_list_max = 0
    
    while True:
        if is_sorted(old_list, new_list_max):
            print(move_count)
            break

        min_item = min(old_list)
        old_list.remove(min_item)
        new_val = max(min_item+1, new_list_max+1)
        new_list_max = new_val
        new_list.append(new_val)
        move_count += new_val - min_item

##    print(new_list+old_list)
    return


##
##  Main routine
##
if __name__ == '__main__':
    
    tc = TestCase()
    tc.t = int(sys.stdin.readline())
    
    for i in range(tc.t):
        solve(tc)
