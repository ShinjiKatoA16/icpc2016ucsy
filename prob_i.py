#!/usr/bin/python3
# -*- coding: utf-8 -*-

'''
    2016 ICPC at UCSY
    Problem-I: Clustering
'''
import sys


class TestCase():
    pass

class CellData():
    ## Class Method
    def prep_matrix(row, col):
        '''
        row: y-axis size of matrix
        col: x-axis size of matrix
        Initialize matrix List of CellData objects. Need to be called before
        CellData Object creation
        [[None, None,...], [None, None,...],...]
        '''
        CellData.matrix_size_r = row
        CellData.matrix_size_c = col
        CellData.matrix = [[None for c in range(col)] for r in range(row)]
        return

    ## Instance Method
    def __init__(self, row, col, val):
        '''
        row: y-axis size of matrix
        col: x-axis size of matrix
        val: 0: Not a cluster, 1: part of cluster
        '''
        self.r = row
        self.c = col
        self.val = val
        self.cluster = None   ## Cluster Number
        self.neibour = list()
        CellData.matrix[row][col] = self
        return

        
    def append_neibour(self):
        '''
        self: own object
        set up 8 neibour object to own object
        '''
        for r in range(self.r-1,self.r+2):
            for c in range(self.c-1,self.c+2):
                if r <0 or c <0:
                    self.neibour.append(None)
                elif r >= CellData.matrix_size_r or c >= CellData.matrix_size_c:
                    self.neibour.append(None)
                elif r == self.r and c == self.c:
                    continue 
                else:
                    self.neibour.append(CellData.matrix[r][c])
        return


    def set_cluster(self, cluster):
        '''
        self: own object
        cluster: cluster number
        set cluster number and recurse to neibour objects
        '''
        if self.cluster == cluster:
            return
        elif self.cluster != None:
            print ('Logic error in set_cluster', cluster, self.cluster, self.r, self.c)
            assert self.cluster == None
        else:
            self.cluster = cluster
            for neibour in self.neibour:
                if neibour != None and neibour.val == 1:
                    neibour.set_cluster(cluster)
        return


def parse_tc(tc):
    '''
        Input: Test Case
        Update: Start Location, Delivery List
        Return: None
    '''

    tc.matrix = list()
    (tc.row, tc.col) = map(int,sys.stdin.readline().split())
    for i in range(tc.row):
        tc.matrix.append(tuple(map(int,sys.stdin.readline().split())))

    return


def solve(tc):
    '''
        Input: Test Case
        Return: None
    '''

    parse_tc(tc)
    CellData.prep_matrix(tc.row, tc.col)

    for r in range(tc.row):
        for c in range(tc.col):
            cell = CellData(r, c, tc.matrix[r][c])

    for r in range(tc.row):
        for c in range(tc.col):
            cell = CellData.matrix[r][c]
            cell.append_neibour()        ## keep 8 adjustcent cell in list

    num_cluster = 0
    for r in range(tc.row):
        for c in range(tc.col):
            cell = CellData.matrix[r][c]
            if cell.val == 1 and cell.cluster == None:
                num_cluster += 1
                cell.set_cluster(num_cluster)
    print(num_cluster)

    return


##
##  Main routine
##
if __name__ == '__main__':
    tc = TestCase()
    tc.t = int(sys.stdin.readline())
    
    for i in range(tc.t):
        solve(tc)
