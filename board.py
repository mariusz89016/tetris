#!/usr/local/bin/python
# -*- coding: utf-8 -*-
import copy
import os
import random
from time import sleep

from block import Block, four_block, vertical_four, horizontal_four


class Board:
    def __init__(self, x, y):
        self.block_x = 3
        self.block_y = 0
        self.block = None
        self.x = x
        self.y = y
        self.tab = [[None for _ in range(x)] for _ in range(y)]
        self.tab.append([True for _ in range(x)])

    def start(self):
        f = Block(four_block)
        v = Block(vertical_four)
        h = Block(horizontal_four)
        blocks = [f, v, h, f, v, h, f, v, h, f, v, h, f, v, h]

        for block in blocks:
            self._fall_one_block(block)

    def move_left(self):
        self.block_x -= 1
        os.system("clear")
        self.show_board_with_block(self.block, self.block_x, self.block_y)

    def move_right(self):
        self.block_x += 1
        os.system("clear")
        self.show_board_with_block(self.block, self.block_x, self.block_y)

    def _fall_one_block(self, block):
        self.block = block
        self.block_x = random.randint(0, 4)
        self.block_y = 0
        while True:
            os.system("clear")
            self.show_board_with_block(block, self.block_x, self.block_y)
            if self.collide(block, self.block_x, self.block_y + 1):
                self.put_block(block, self.block_x, self.block_y)
                self.remove_full_lines()
                break
            self.block_y += 1
            sleep(0.4)

    def __str__(self, *args, **kwargs):
        return Board._get_string_tab(self.tab)

    @staticmethod
    def _get_string_tab(tab):
        result = ''
        for y in tab[:-1]:
            result += '|'
            for x in y:
                result += ' ' if x is None else '█'
            result += '|\n'
        result += ' ' + ''.join(['‾' for _ in range(len(tab[0]))]) + ' '
        return result

    def show_board_with_block(self, block, x, y):
        new_tab = copy.deepcopy(self.tab)
        for j in range(len(block.get_array())):
            for i in range(len(block.get_array()[0])):
                if y + j < self.y and x + i < self.x:
                    new_tab[y + j][x + i] = True
        print(Board._get_string_tab(new_tab))

    def put_block(self, block, x, y):
        for j in range(len(block.get_array())):
            for i in range(len(block.get_array()[0])):
                self.tab[y + j][x + i] = True

    def collide(self, block, x, y):
        for j in range(len(block.get_array()) - 1, -1, -1):
            for i in range(len(block.get_array()[0])):
                if self.tab[y + j][x + i] and block.get_array()[j][i]:
                    return True
        return False

    def remove_full_lines(self):
        #self.tab = self.tab[:-1]
        #self.tab.insert(0, [None for _ in range(self.x)])
        # self.tab[self.x - 1] = [None for _ in range(self.x)]
        pass
