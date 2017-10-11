#!/usr/bin/python3
# -*- coding: utf-8 -*-

'''
    2016 ICPC at UCSY
    Problem-K: One Time Pad
'''
import sys


class TestCase():
    pass


def parse_tc(tc):
    '''
        Input: Test Case
        Update: Message, Shift_num
        Return: None
    '''

    tc.msg = sys.stdin.readline().split('\n')[0]
    tc.num = list(map(int,sys.stdin.readline().split()))

    assert len(tc.msg) == len(tc.num),'Input message and shift number mismatch'

    return


def solve(tc):
    '''
        Input: Test Case
        Return: None
    '''

    import string

    ALPHABET = 2 * string.ascii_lowercase
    parse_tc(tc)

    out = ''
    for i in range(len(tc.msg)):
        orig_char = tc.msg[i]
        if orig_char not in ALPHABET:
            out += '?'
            continue
        else:
            pos = ALPHABET.index(orig_char)

        offset = tc.num[i] % (len(ALPHABET) // 2)
        out += ALPHABET[pos + offset: pos + offset + 1]

    print(out)
    return


##
##  Main routine
##
if __name__ == '__main__':
    tc = TestCase()
    tc.t = int(sys.stdin.readline())
    
    for i in range(tc.t):
        solve(tc)
