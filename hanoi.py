#!/usr/bin/python3
# -*- coding: utf-8 -*-

# Tower of hanoi

hanoi_called = 0
hanoi_moved = 0

def hanoi(num, from_pos, to_pos, tmp_pos):
    '''
    num: Number of moving blocks, 1: Only top block
    from_pos: move from
    to_pos: move to
    tmp_pos: temporary position
    '''
    global hanoi_called
    global hanoi_moved
    hanoi_called += 1

    # print('Num:', num, 'From:',str(from_list),'To:', str(to_list), 'Temp:', str(tmp_list))
    if num < 0:
        raise ValueError

    if num == 1:
        block = from_pos.pop()
        to_pos.append(block)
        hanoi_moved += 1
        print(str(from_list), str(to_list), str(tmp_list))
    else:
        hanoi(num-1, from_pos, tmp_pos, to_pos)
        hanoi(1, from_pos, to_pos, tmp_pos)
        hanoi(num-1, tmp_pos, to_pos, from_pos)


number_of_floor = 8
from_list = [n for n in range(number_of_floor,0,-1)]
to_list = []
tmp_list = []

hanoi(number_of_floor, from_list, to_list, tmp_list)
print ('Number of hanoi() called', hanoi_called, 'Block moved', hanoi_moved)
