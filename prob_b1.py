#!/usr/bin/python3
# -*- coding: utf-8 -*-

'''
    2016 ICPC at UCSY
    Problem-B: The Election (without unlimited interger version)
'''
import sys
BIG_PRIME_NUMBER = 10**9+7


class TestCase():
    pass


def parse_tc(tc):
    '''
        Input: class of Test Case
        Update: n, x_i, q, query in test case
        Return: None
    '''

    tc.query = list()

    tc.n = int(sys.stdin.readline())
    tc.x_i = list(map(int,sys.stdin.readline().split()))
    if (len(tc.x_i) != tc.n):
        print('Invalid input: number of account')
        assert False
    tc.q = int(sys.stdin.readline())
    for i in range(tc.q):
        s = sys.stdin.readline()
        query = list(map(int,s.split()))

        if (query[0] == 1):
            if len(query) != 5:
                print('Invalid query-1 data', s)
                assert False
        elif (query[0] == 2):
            if len(query) != 2:
                print('Invalid query-2 data', s)
                assert False
        else:
            print('Unknown query data', s)
            assert False

        tc.query.append(query)

    return


def prod_bigN(gain, rate):

    overflow = 0
    for idx in range(len(gain)):
        temp = gain[idx] * rate + overflow
        overflow = temp // BIG_PRIME_NUMBER
        gain[idx] = temp % BIG_PRIME_NUMBER

    if overflow != 0:
        gain.append(overflow)

#    print(gain)

    return


def calc_gain(base, rate, exp):

    gain = [base]

    for i in range(exp):
        prod_bigN(gain, rate)

    return gain


def is_bigger(a, b):
    '''
    a: list of n-ary number
    b: list of n-ary number
    return True if a>b
           False otherwise
    '''

    if len(a) > len(b):
        return True
    elif len(b) > len(a):
        return False
    else:               # same length
        idx = len(a) - 1
        while idx >= 0:
            if a[idx] > b[idx]:
                return True
            elif b[idx] > a[idx]:
                return False
            idx -= 1

        return False    # same number

    assert False        # never happen

def search_best(tc, voter, manufesto):
    best_gain = []
    best_candidate = 0

    for m in manufesto:
        if voter > m[1] and voter <= m[2]:
            gain = calc_gain(tc.x_i[voter-1], m[3], voter - m[1])
            if is_bigger(gain, best_gain):
                best_gain = gain
                best_candidate = m[4]

    if best_gain == []:
        print(-1)
    else:
        print(best_candidate, best_gain[0])

    return

def solve(tc_num, tc):
    '''
        Input: Test Case
        Return: None
    '''

    print('Case ',tc_num+1,':',sep='')
    parse_tc(tc)
    manufesto = list()
    for q in tc.query:
        if q[0] == 1:  ## Manufesto
            manufesto.append(q)
        elif q[0] == 2:  ## voter
            search_best(tc, q[1], manufesto)
        else:
            print('Logic error')
            assert False

    return


##
##  Main routine
##
if __name__ == '__main__':
    tc = TestCase()
    tc.t = int(sys.stdin.readline())
    
    for i in range(tc.t):
        solve(i, tc)
