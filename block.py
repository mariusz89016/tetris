#!/usr/local/bin/python
# -*- coding: utf-8 -*-

class Block:
    def __init__(self, elem):
        self.elem = elem

    def __str__(self):
        result = ''
        for y in range(len(self.elem)):
            for x in range(len(self.elem[0])):
                result += '█' if self.elem[y][x] else ' '
            result += '\n'
        return result

    def get_array(self):
        return self.elem


# ◼
left_four = [[True, False], [True, True], [False, True]]
right_four = [[False, False], [True, True], [True, False]]
four_block = [[True, True], [True, True]]
vertical_four = [[True], [True], [True], [True]]
horizontal_four = [[True, True, True, True]]
