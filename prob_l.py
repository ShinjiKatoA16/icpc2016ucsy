#!/usr/bin/python3
# -*- coding: utf-8 -*-

'''
    2016 ICPC at UCSY
    Problem-L: Password for Sweethearts
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

    tc.names = sys.stdin.readline().split()

    assert (len(tc.names) == 2),'Invalid input'

    return


def num_bit1(n):
    '''
        Input: Non Negative Integer
        Return: count of 1b
    '''

    bit1_count = 0
    while n > 0:
        if n & 0x00000001:   ## bit and
            bit1_count += 1
        n //= 2     ## n = n >> 1
    return bit1_count


def mix_2str(list1, list2, bitmap):
    '''
        list1: List of 1 char string
        list2: List of 1 char string
        bitmap: Integer, 1b in each position represent List1 str
        Return: Combined string
    '''

    mixed_str = ''
    list1_pos = 0
    list2_pos = 0

    while bitmap > 0:
        if bitmap & 0x00000001:
            mixed_str += list1[list1_pos]
            list1_pos += 1
        else:
            mixed_str += list2[list2_pos]
            list2_pos += 1
        bitmap //= 2

    while list2_pos < len(list2):
        mixed_str += list2[list2_pos]
        list2_pos += 1

    return  mixed_str


def solve(tc):
    '''
        Input: Test Case
        Return: None
    '''

    parse_tc(tc)

    total_pw = 0
    new_pw = list()

    name1 = list(tc.names[0])
    name2 = list(tc.names[1])
    len_name1 = len(name1)
    len_name2 = len(name2)

    for i in range(2**(len_name1+len_name2)):
        if num_bit1(i) != len_name1: continue
        mixed_str = mix_2str(name1, name2, i)
        if mixed_str not in new_pw:
            new_pw.append(mixed_str)
            print(mixed_str)
            total_pw += 1

    print(total_pw)
    return


##
##  Main routine
##
if __name__ == '__main__':
    tc = TestCase()
    tc.t = int(sys.stdin.readline())
    
    for i in range(tc.t):
        solve(tc)
