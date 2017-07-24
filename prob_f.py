#!/usr/bin/python3
# -*- coding: utf-8 -*-

'''
    2016 ICPC at UCSY
    Problem-F: Chocolates
    Jul/24/2017. under construction
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

    tc.num_type = int(sys.stdin.readline())
    tc.weights = list(map(int,sys.stdin.readline().split()))
    if tc.num_type != len(tc.weights):
        print('Input data mismatch', tc.num_type, tc.weights)
        raise ValueError

    tc.num_query = int(sys.stdin.readline())
    tc.num_people = list(map(int,sys.stdin.readline().split()))
    if tc.num_query != len(tc.num_people):
        print('Input data mismatch', tc.num_query, tc.num_people)
        raise ValueError

    return

def min_weight(num_type, w_list, num_people):
    if num_type == 1:
        if tc_num_people[i] == 1:
            return w_list[0]
        else:
            return 'NONE'


def solve(tc):
    '''
        Input: Test Case
        Return: None
    '''

    parse_tc(tc)
    tc.weights.sort()

    for i in range(tc.query):
        print(min_weight(tc.num_type, tc.weight, tc_num_people[i]))

    return


##
##  Main routine
##
if __name__ == '__main__':
    
    tc = TestCase()
    tc.t = int(sys.stdin.readline())
    
    for i in range(tc.t):
        print('Case ', i, ':', sep='')
        solve(tc)
