#!/usr/bin/python

import thread

import time

from board import Board
from getch import Getch

board = Board(10, 10)


def get_input():
    getch = Getch()
    while True:
        ch = getch(3)
        # elif k=='\x1b[B':
        #         print "down"
        if ch == '\x1b[C':
            board.move_right()
        if ch == '\x1b[D':
            board.move_left()


def play():
    board.start()
    # sys.exit(1)


try:
    x = thread.start_new_thread(get_input, ())
    y = thread.start_new_thread(play, ())
except:
    print("asd")

time.sleep(20)
