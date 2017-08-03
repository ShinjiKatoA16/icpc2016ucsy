#!/usr/bin/python3
# -*- coding: utf-8 -*-

'''
    2016 ICPC at UCSY
    Problem-A: Evaluating Fully Parenthesized Expression
               This version relys on Python's eval() function,
               which does not exist in many language. unfair :-)
               I will make another version that can be converted to
               other languages later
'''
import sys


class TestCase():
    pass


def str2token(formula):
    '''
        input: String
        return: List of Token
    '''
    digit = ''
    token_list = list() 

#    print(formula, file=sys.stderr)
    for c in formula:
        if c in '()+-*/':
            if digit != '':
                token_list.append(digit)
                digit = ''
            token_list.append(c)
        elif c in '0123456789':
            digit += c
        elif c in '\n':
            if digit != '':
                token_list.append(digit)
                digit = ''
        else:
            raise ValueError

#    print(token_list, file=sys.stderr)
    return token_list


def token2list(token_list):
    '''
        input: List of Token
        return: Up to 3 element list, each element may be a list
    '''
#    print('token2list:',token_list, file=sys.stderr)
    nested_list = list()
    p = 0
    while p < len(token_list):
        if token_list[p] == '(':
            open_p = 1
            for q in range(p+1,len(token_list)):
                if token_list[q] == ')':
                    open_p -= 1
                    if open_p == 0:   # matching close paren found
                        break
                elif token_list[q] == '(':
                    open_p += 1

            if open_p != 0:
                print('Improper input file, number of parentesis not match')
                raise ValueError

            nested_list.append(token2list(token_list[p+1:q]))
            p = q
        elif token_list[p] in '+-*/':
            nested_list.append(token_list[p])
        else:
            nested_list.append(float(token_list[p]))

        p += 1

#    print(nested_list, file=sys.stderr)
    return nested_list

def eval_list(nested_list):
    '''
        input: List contains up to 3 element
        return: Evaluated value of the list
    '''
    for i in range(len(nested_list)):
        if type(nested_list[i]) == type(list()):
            nested_list[i] = eval_list(nested_list[i])

    if len(nested_list) == 1:
        if type(nested_list[0]) != type(0.0):
            print('Logic error', nested_list)
            raise ValueError
        return nested_list[0]

    elif len(nested_list) == 2:  # +xxx or -xxx
        if nested_list[0] not in '+-':
            print('Logic error', nested_list)
            raise ValueError

        if nested_list[0] == '-':
            return -1 * nested_list[1]
        else:
            return rested_list[1]

    elif len(nested_list) == 3:  # xxx operator yyy
        if nested_list[1] not in '+-*/':
            print('Logic error', nested_list)
            raise ValueError
        if nested_list[1] == '+':
            return nested_list[0] + nested_list[2]
        elif nested_list[1] == '-':
            return nested_list[0] - nested_list[2]
        elif nested_list[1] == '*':
            return nested_list[0] * nested_list[2]
        elif nested_list[1] == '/':
            return nested_list[0] / nested_list[2]

    print('Logic error', nested_list)
    raise ValueError


def eval_formula(formula):
    '''
        input: String
        output: evalated value

        example: '(1+(23*345))\n'
        1. Convert String to flat list of Tokens
                 ['(','1','+','(','23','*','345',')',')']
        2. Convert the flat list to nested list, each list has up to 3 element
                 ['1','+',['23','*','345']]
        3. Evaluate the nested list
    '''

    token_list = str2token(formula)
    nested_list = token2list(token_list)
    return eval_list(nested_list)

def solve(tc):
    '''
        Input: Test Case
        Return: None
    '''

    try:
    ##    result = eval(sys.stdin.readline())
        result = eval_formula(sys.stdin.readline())
    except ZeroDivisionError:
        print('Infinity')
    else:
        print(float(result))
    return


##
##  Main routine
##
if __name__ == '__main__':
    tc = TestCase()
    tc.t = int(sys.stdin.readline())
    
    for i in range(tc.t):
        solve(tc)
