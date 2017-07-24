#!/usr/bin/python3
# -*- coding: utf-8 -*-

'''
    2016 ICPC at UCSY
    Problem-H: Like Father Like Son
'''
import sys

N_DIGITS = 14     ## round() accuracy
## THETA = 2*(10**(-14))

class TestCase():
    pass


class polygon():
    def __init__(self, name, num_vertex):
        self.name = name
        self.num_vertex = num_vertex
        self.vertex = list()
        self.vector_sets = list()
        self.longest_edge = 0
        return

    def add_vertex(self, x, y):
        self.vertex.append(tuple((x, y)))
        return

    def calc_longest_edge(self):

        def distance(p0, p1):
            d = ((p0[0]-p1[0])**2+(p0[1]-p1[1])**2) **0.5
            return ((p0[0]-p1[0])**2+(p0[1]-p1[1])**2) **0.5

        self.longest_edge = distance(self.vertex[-1], self.vertex[0])
        for i in range(0, len(self.vertex)-1):
            self.longest_edge = max(self.longest_edge,
                                   distance(self.vertex[i], self.vertex[i+1]))
        return

    def calc_vectors(self, num_variant=7):

        def normalize_vector(variant, longest_edge):
            origin = min(variant)
            origin_pos = variant.index(origin)
            variant = variant[origin_pos:] + variant[:origin_pos]

            for i in range(len(variant)):
                x, y = variant[i]
                x0, y0 = origin
                x = round((x-x0)/longest_edge, N_DIGITS)
                y = round((y-y0)/longest_edge, N_DIGITS)
                variant[i] = tuple((x, y))

            return variant

        self.calc_longest_edge()
        variant = self.vertex[:]
        v = normalize_vector(variant, self.longest_edge)
        self.vector_sets.append(v)

        if num_variant == 0:
            return

        for i in range(3):
            ## rotate 90 degree
            for i in range(len(variant)):
                x, y = variant[i]
                variant[i] = (-y, x)
            v = normalize_vector(variant, self.longest_edge)   ## change origin
            self.vector_sets.append(v)

        for i in range(4):
            ## mirror
            variant = self.vector_sets[i]
            variant.reverse()
            for i in range(len(variant)):
                x, y = variant[i]
                variant[i] = (x, -y)
            v = normalize_vector(variant, 1)   ## change origin, remain length
            self.vector_sets.append(v)



def parse_tc(tc):
    '''
        Input: Test Case
        Update: Start Location, Delivery List
        Return: None
    '''

    father, s = sys.stdin.readline().split()
    if father != 'F':
        raise ValueError('First char is not F')
    num_father = int(s)

    tc.fathers = list()
    tc.sons = list()

    for i in range(num_father):
        p_name, num_vertex = sys.stdin.readline().split()
        num_vertex = int(num_vertex)
        p = polygon(p_name, num_vertex)
        tc.fathers.append(p)
        for v in range(num_vertex):
            x, y = map(float, sys.stdin.readline().split())
            p.add_vertex(x, y)

    son, s = sys.stdin.readline().split()
    if son != 'S':
        print(son, s)
        raise ValueError('First char is not S')
    num_son = int(s)

    for i in range(num_son):
        p_name, num_vertex = sys.stdin.readline().split()
        num_vertex = int(num_vertex)
        p = polygon(p_name, num_vertex)
        tc.sons.append(p)
        for v in range(num_vertex):
            x, y = map(float, sys.stdin.readline().split())
            p.add_vertex(x, y)

    return


def match(f, s):
    if f.longest_edge < s.longest_edge:
        return False

    for vector_list in f.vector_sets:
        if s.vector_sets[0] == vector_list:
            return True

    return False


def solve(tc):
    '''
        Input: Test Case
        Return: None
    '''

    parse_tc(tc)

    for f in tc.fathers:
        print(f.name, end='')
        f.calc_vectors()   ## cacl all posiible vector sets

        for s in tc.sons:
            s.calc_vectors(0)  ## number of variant=Rotation/reverse
            if match(f, s):
                print(' ', s.name, sep='', end='')
        print()

    return


##
##  Main routine
##
if __name__ == '__main__':
    
    tc = TestCase()
    
    solve(tc)
