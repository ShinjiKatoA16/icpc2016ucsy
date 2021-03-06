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
        Update: Names in Test case
        Return: None
    '''

    tc.names = sys.stdin.readline().split()

    assert (len(tc.names) == 3),'Invalid input'

    return


def num_digit(n):
    '''
        Input: Non Negative Tenary integer
        Return: count of 2 and count of 1 
    '''

    digit2_count = 0
    digit1_count = 0

    while n > 0:
        digit = n % 3
        if digit == 2:
            digit2_count += 1
        elif digit == 1:
            digit1_count += 1
        n //= 3     ## n = n >> 1

    return digit2_count, digit1_count


def mix_3str(str0, str1, str2, bitmap):
    '''
        str0: Name of first person
        str1: Name of second person
        str2: Name of third person
        bitmap: Tenary Integer, 2: str0, 1: str1, 0: str2
        Return: Combined string
    '''

    mixed_str = ''
    str0_pos = 0
    str1_pos = 0
    str2_pos = 0

    while bitmap > 0:
        digit = bitmap % 3
        if digit == 2:
            mixed_str += str2[str2_pos]
            str2_pos += 1
        elif digit == 1:
            mixed_str += str1[str1_pos]
            str1_pos += 1
        else:
            mixed_str += str0[str0_pos]
            str0_pos += 1
        bitmap //= 3

    while str0_pos < len(str0):
        mixed_str += str0[str0_pos]
        str0_pos += 1

    return  mixed_str


def solve(tc):
    '''
        Input: Test Case
        Return: None
    '''

    parse_tc(tc)

    total_pw = 0
    new_pw = dict()

    name0 = tc.names[0]
    name1 = tc.names[1]
    name2 = tc.names[2]
    len_name0 = len(name0)
    len_name1 = len(name1)
    len_name2 = len(name2)

    for i in range(3**(len_name0+len_name1+len_name2)):
        num_digit2, num_digit1 = num_digit(i)
        if num_digit2 != len_name2: continue
        if num_digit1 != len_name1: continue
        mixed_str = mix_3str(name0, name1, name2, i)
        if mixed_str not in new_pw:
            new_pw[mixed_str] = True
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
