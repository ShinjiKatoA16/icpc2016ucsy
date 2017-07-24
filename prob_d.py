#!/usr/bin/python3
# -*- coding: utf-8 -*-

'''
    2016 ICPC at UCSY
    Problem-D: Bakery Delivery Scheduler
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

    tc.deliveryList = list()
    tc.startLocation = 0

    while True:
        END_OF_DATA = -999
        loc = int(sys.stdin.readline())
        if loc == END_OF_DATA: break
        tc.deliveryList.append(loc)

    tc.startLocation = int(sys.stdin.readline())

    return


def solve(tc):
    '''
        Input: class of Test Case
        Return: None
    '''

    parse_tc(tc)
    upward = list()
    downward = list()

    for i in tc.deliveryList:
        if i > tc.startLocation:
            upward.append(i - tc.startLocation)
        else:
            downward.append(tc.startLocation - i)

    if (len(upward) == 0): up_max = 0
    else: up_max = max(upward)

    if (len(downward) == 0): down_max = 0
    else: down_max = max(downward)

    if up_max < down_max:
        if up_max != 0: print('Upward_First')
        else: print('Downward_First')
        total_distance = up_max * 2 + down_max
    else:
        if down_max != 0: print('Downward_First')
        else: print('Upward_First')
        total_distance = down_max * 2 + up_max

    print(total_distance)
    return


##
##  Main routine
##
if __name__ == '__main__':
    tc = TestCase()
    tc.t = int(sys.stdin.readline())
    
    for i in range(tc.t):
        solve(tc)
