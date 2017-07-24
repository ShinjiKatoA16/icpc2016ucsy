#!/usr/bin/python3
# -*- coding: utf-8 -*-

'''
    2016 ICPC at UCSY
    Problem-E: Tree Pendant
'''
import sys
EDGE_GOLD = 0
EDGE_SILVER = 1


class TestCase():
    pass


class Nexus():
    def __init__(self, node_obj, partner, edge):
        self.node_obj = node_obj
        self.partner = partner
        self.edge = edge
        return


def flip_color(color):
    if color == EDGE_GOLD:
        return EDGE_SILVER
    elif color == EDGE_SILVER:
        return EDGE_GOLD
    else:
        assert False, 'logic error: flip_color'


class Node():
    def init_memberlist():
        Node.members = list()
        Node.member_id = list()

    def __init__(self, my_id):
        self.id = my_id
        self.connection = list()
        self.nexus_count = 0
        Node.members.append(self)
        Node.member_id.append(self.id)

    def add_connection(self, partner, edge):
        nexus = Nexus(self, partner, edge)
        self.connection.append(nexus)
        self.nexus_count += 1
        return

    def remove_connection(self, partner):
        for nexus in self.connection:
            if nexus.partner == partner:
                self.connection.remove(nexus)
                self.nexus_count -= 1
                return
        print('remove_connection: Invalide request:', partner.id)
        raise ValueError
        return

    def get_edge(self, partner):
        for nexus in self.connection:
            if nexus.partner == partner:
                return nexus.edge
        return None

    def set_edge(self, partner, edge):
        for nexus in self.connection:
            if nexus.partner == partner:
                nexus.edge = edge
        else:
            print('set_edge: Partner:', partner.id)
            raise ValueError 

    def find_path(self, target_id, origin=None):
        for nexus in self.connection:
            if nexus.partner.id == target_id:
                return [nexus]
            elif nexus.partner == origin:
                continue
            elif nexus.partner.nexus_count > 1:
                nexuspath = nexus.partner.find_path(target_id, self)
                if nexuspath:
                    nexuspath.append(nexus)
                    return nexuspath
        return False

    def check_tree(self, ignore_id=None):
        num_gold = 0
        num_silver = 0
        for nexus in self.connection:
            if nexus.partner.id == ignore_id:
                continue

            if nexus.edge == EDGE_GOLD:
                num_gold += 1
            elif nexus.edge == EDGE_SILVER:
                num_silver += 1
            else:
                assert False, 'Logic error in check_tree'

            if nexus.partner.nexus_count > 1:
                g, s = nexus.partner.check_tree(self.id)
                num_gold += g
                num_silver += s

        return (num_gold, num_silver)

    def reverse_tree_color(self, ignore_id = None):
        for nexus in self.connection:
            if nexus.partner.id == ignore_id:
                continue

            nexus.edge = flip_color(nexus.edge)
            
            if nexus.partner.nexus_count > 1:
                nexus.partner.reverse_tree_color(self.id)

        return
              


def parse_tc(tc):
    '''
        Input: Test Case
        Update: Connection List, Query List
        Return: None
    '''

    header = sys.stdin.readline()
    if not header: return True    ## EOF

    n, q = map(int, header.split())
    tc.connection = list()
    tc.query = list()

    for i in range(n-1):
        tc.connection.append(tuple(map(int, sys.stdin.readline().split())))

    for i in range(q):
        tc.query.append(tuple(map(int, sys.stdin.readline().split())))

    return False


def print_nodes():
    print('Display node information')
    for n in Node.members:
        print(n.id, n.nexus_count)
        for c in n.connection:
            print(c.partner.id, c.edge, end='   ')
        print()


def id_index(id):
    if id not in Node.member_id:
        obj = Node(id)

    index = Node.member_id.index(id)
    assert Node.members[index].id == id, 'Logic error, id_index()'
    return index


def id2node(id):
    return Node.members[id_index(id)]


def set_color(u, v, k):
    color = k
    ## create path list [nexus-to-u, ... nexus_to_v]
    node_u = id2node(u)
    node_v = id2node(v)
    nexus_uv_path = node_u.find_path(v)
    nexus_uv_path.reverse()
    assert nexus_uv_path[0].node_obj.id == u, 'Logic error: set_color'

    for nexus in nexus_uv_path:
        next_id = nexus.partner.id
        nexus.edge = color
        color = flip_color(color)

    if next_id != v:
        print('set_color: Logic error, last id:', next_id) 
        assert False

    nexus_vu_path = node_v.find_path(u)

    color = k
    for nexus in nexus_vu_path:
        next_id = nexus.partner.id
        nexus.edge = color
        color = flip_color(color)

    return


def reattach(u, v, w):
    node_u = id2node(u)
    node_v = id2node(v)
    node_w = id2node(w)

    nexus_uv = node_u.find_path(v)
    assert nexus_uv[0].partner.id == v, 'Logic error: reattach'
    color_uv = nexus_uv[0].edge

    node_u.remove_connection(node_v)
    node_v.remove_connection(node_u)

    node_v.reverse_tree_color()

    node_v.add_connection(node_w, color_uv)
    node_w.add_connection(node_v, color_uv)


def pathstats(u, v):
    num_gold = 0
    num_silver = 0

    node_u = id2node(u)
    nexus_path = node_u.find_path(v)
    for nexus in nexus_path:
        if nexus.edge == EDGE_GOLD:
            num_gold += 1
        elif nexus.edge == EDGE_SILVER:
            num_silver += 1
        else:
            print('Logic error. edge color invalid', nexus.edge)
            assert False

    print(num_gold, num_silver)
    return


def treestats(u, v):

    node_u = id2node(u)
    if u == v:
        num_gold, num_silver = node_u.check_tree(None)
    else:
        node_v = id2node(v)
        nexus_path = node_v.find_path(u)
        if nexus_path[0].partner.id != u:
            print('Logic error', nexus_path[0].partner.id, u)
            assert False

        num_gold, num_silver = node_u.check_tree(nexus_path[0].node_obj.id)
    print(num_gold, num_silver)


def solve(tc):
    '''
        Input: Test Case
        Return: None
    '''

    if parse_tc(tc): return True

    tc.case_num += 1
    print('Case ', tc.case_num, ':', sep='')

##    print(tc.connection)
##    print(tc.query)

    Node.init_memberlist()

    for x in tc.connection:
        id1, id2, edge = x

        node1 = id2node(id1)
        node2 = id2node(id2)
        node1.add_connection(node2, edge)
        node2.add_connection(node1, edge)

##    print_nodes()
    for q in tc.query:
        if q[0] == 1:
            if q[3] != EDGE_GOLD and q[3] != EDGE_SILVER:
                print('Invalid color: %d', q[3])
                raise ValueError
            set_color(q[1], q[2], q[3])
        elif q[0] == 2:
            reattach(q[1], q[2], q[3])
        elif q[0] == 3:
            pathstats(q[1], q[2])
        elif q[0] == 4:
            treestats(q[1], q[2])
        else:
            print('Invalid query: %d', q[0])
            raise ValueError

    
    return False


##
##  Main routine
##
if __name__ == '__main__':
    
    tc = TestCase()
    tc.case_num = 0
    
    while True:
        if solve(tc) == True:
            break

