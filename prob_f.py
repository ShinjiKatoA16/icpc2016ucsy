#!/usr/bin/python3
# -*- coding: utf-8 -*-

'''
    2016 ICPC at UCSY
    Problem-F: Chocolates
    Jul/24/2017. under construction
'''
import sys

MAX_N = 5  # Max nuumber of chocolate type
MAX_wi = 11  # Max weight of chocolate


def gcd(a, b):
    '''
    a: Positive integer
    b: Positive integer
    return Greatest Common Divisor of a and b
    '''
    while b>0:
        a, b = b, a%b
    return a


def lcm(a, b):
    '''
    a: Positive integer
    b: Positive integer
    return Least Common Multiple of a and b
    '''
    return a*b // gcd(a, b)


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
    min_w = w_list[0]
    if num_people == 1:
        return min_w

    if num_type == 1:
        return 'NONE'
    elif num_type == 2:
        return (num_people-1) * lcm(w_list[0], w_list[1])

    num_list = [[0 for n in range(MAX_N+1)] for i in range(MAX_wi)]

    num_list[0][0] = 1   # Total:0 Num of compination: 1
    num_list_top = 0

    while True:
        for w_index in range(len(w_list)):
            w = w_list[w_index]
            num_list[w][MAX_N] = 0  # Total of the weight
            for n in range(MAX_N):
                if w_index >= n:
                    num_list[w][w_index] += num_list[0][n]
                num_list[w][MAX_N] += num_list[w][n]

            if num_list[w][MAX_N] >= num_people:
                return (w + num_list_top)


        nonzero_index = 1
        while True:
            if num_list[nonzero_index][MAX_N]:
                break
            nonzero_index += 1

        num_list_top += nonzero_index
        num_list = num_list[nonzero_index:nonzero_index+MAX_wi]
        for i in range(nonzero_index):
            num_list.append([0,0,0,0,0,0])


def solve(tc):
    '''
        Input: Test Case
        Return: None
    '''

    parse_tc(tc)
    tc.weights.sort()

    for i in range(tc.num_query):
        print(min_weight(tc.num_type, tc.weights, tc.num_people[i]))

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
