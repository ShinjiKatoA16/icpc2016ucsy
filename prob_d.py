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

    END_OF_DATA = -999
    while True:
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

    up_most = max(tc.deliveryList)
    down_most = min(tc.deliveryList)

    if tc.startLocation <= down_most:
        print('Upward_First')
        total_distance = up_most - tc.startLocation
    elif tc.startLocation >= up_most: 
        print('Downward_First')
        total_distance = tc.startLocation - down_most
    else:
        up_distance = up_most - tc.startLocation
        down_distance = tc.startLocation - down_most
        
        if up_distance < down_distance:
            print('Upward_First')
            total_distance = up_distance * 2 + down_distance
        else:
            print('Downward_First')
            total_distance = down_distance * 2 + up_distance

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
