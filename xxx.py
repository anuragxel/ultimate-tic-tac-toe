#!/usr/bin/python
#
# Negamax variant of minmax
#
# This program is for demonstration purposes, and contains ample
# opportunities for speed and efficiency improvements.
#
# Also, a minmax tree is not the best way to program a tic-tac-toe
# player.
#
# This software is hereby granted to the Public Domain
#

import sys,os
import random
import numpy as np
import json

# from_file=np.genfromtxt("foo.csv",delimiter=",")
# all_state=np.array(from_file).tolist()
# print states


# for i in from_file:
#     all_state.append(i)


INFINITY=99999999

def numStr(n):
    if n == INFINITY: return "+INFINITY"
    elif n == -INFINITY: return "-INFINITY"
    return str(n)

def write_to_file():
    global states
    global f
    json.dump(states,f)
    f.close()
    #print states

    # final_add = []
    # # print states
    # # print all_state
    # print to_print
    # for e in all_state:
    #     if e not in final_add:
    #         final_add.append(e) 
    # np.savetxt("foo.csv",final_add,delimiter=",")

#-------------------------------------------------------------------

class MinMax(object):
    def __init__(self, maxdepth=INFINITY):
        self.bestmove = -1
        self.maxdepth = maxdepth

    def _buildtree_r(self, playboard, curplayer, depth):
        """Recursively build the minmax tree."""

        # figure out the value of the board:

        if depth > self.maxdepth: return 0 # who knows what the future holds

        if curplayer == Board.X:
            otherplayer = Board.O
        else:
            otherplayer = Board.X

        winner = playboard.getWinner()
        if winner == curplayer:
            return INFINITY
        elif winner == otherplayer:
            return -INFINITY
        elif playboard.full():
            return 0   # tie game

        # get a list of possible moves
        movelist = playboard.getCandidateMoves()

        alpha = -INFINITY

        # for all the moves, recursively rate the subtrees, and
        # keep all the results along with the best move:

        salist = []

        for i in movelist:
            # make a copy of the board to mess with
            board2 = playboard.copy()
            board2.move(curplayer, i)  # make the speculative move

            subalpha = -self._buildtree_r(board2, otherplayer, depth+1)
            if alpha < subalpha:
                alpha = subalpha;

            # keep a parallel array to the movelist that shows all the
            # subtree values--we'll chose at random one of the best for
            # our actual move:
            if depth == 0: salist.append(subalpha)

        # if we're at depth 0 and we've explored all the subtrees,
        # it's time to look at the list of moves, gather the ones
        # with the best values, and then choose one at random
        # as our "best move" to actually really play:

        if depth == 0:
            candidate = []
            board_state=''
            for i in range(len(salist)):
                if salist[i] == alpha:
                    candidate.append(movelist[i])




            
            #print("Best score: %s    Candidate moves: %s" % (numStr(alpha), candidate))
            self.bestmove = random.choice(candidate)
            # all_state.append(self.bestmove)
            board_state=playboard.get_board_values()
            states[board_state]=self.bestmove            


        return alpha

    def buildtree(self, board, curplayer):
        self.bestmove = -1
        alpha = self._buildtree_r(board, curplayer, 0)
        return self.bestmove


#-------------------------------------------------------------------

class Board(list):
    """Holds a complete board in self, row-major order."""

    NONE = 0
    X = 1
    O = 2

    def __init__(self):
        for i in range(9): self.append(Board.NONE)

    def copy(self):
        """Clone a board."""

        b = Board()
        for i in range(9):
            b[i] = self[i]

        return b
        
    def move(self, color, pos):
        """Fill a position on the board."""

        self[pos] = color

    def getCandidateMoves(self):
        """Get a list of free moves."""

        clist = []
        for i in range(9):
            if self[i] == Board.NONE:
                clist.append(i)

        return clist

    def full(self):
        """Returns true if the board is full."""
        for i in range(9):
            if self[i] == Board.NONE:
                return False

        return True

    def _check(self, a, b, c):
        if self[a] == self[b] and self[a] == self[c] and self[a] != Board.NONE:
            return self[a]
        return Board.NONE

    def getWinner(self):
        """Figure out who the winner is, if any."""
        winner = self._check(0,1,2)
        if winner != Board.NONE: return winner
        winner = self._check(3,4,5)
        if winner != Board.NONE: return winner
        winner = self._check(6,7,8)
        if winner != Board.NONE: return winner
        winner = self._check(0,3,6)
        if winner != Board.NONE: return winner
        winner = self._check(1,4,7)
        if winner != Board.NONE: return winner
        winner = self._check(2,5,8)
        if winner != Board.NONE: return winner
        winner = self._check(0,4,8)
        if winner != Board.NONE: return winner
        winner = self._check(2,4,6)
        if winner != Board.NONE: return winner

        return Board.NONE
    def get_board_values(self):
        r=''
        for i in range(9):
            
            if self[i] == Board.NONE:
                #r += '%d' % i
                r = r+ '-'
            elif self[i] == Board.X:
                r = r + 'x'
            elif self[i] == Board.O:
                r = r+ 'o'

            # if i == 2:
            #     r += '|  0 1 2\n%s\n' % blank

            # if i == 5:
            #     r += '|  3 4 5\n%s\n' % blank

            # if i == 8:
            #     r += '|  6 7 8\n%s\n' % blank
        return r


    def __str__(self):
        """ Pretty-print the board."""

        blank = '+-+-+-+'
        r = blank + '\n'

        for i in range(9):
            r += '|'
            if self[i] == Board.NONE:
                #r += '%d' % i
                r += ' '
            elif self[i] == Board.X:
                r += 'X'
            elif self[i] == Board.O:
                r += 'O'

            if i == 2:
                r += '|  0 1 2\n%s\n' % blank

            if i == 5:
                r += '|  3 4 5\n%s\n' % blank

            if i == 8:
                r += '|  6 7 8\n%s\n' % blank

        return r

#-------------------------------------------------------------------
# MAIN:

# make the real board we'll be using

def main():
    global f
    global states
    f = open('foo.csv','r+')
    if os.stat("foo.csv").st_size != 0:
        states = json.load(f)
        f.close()
        open('foo.csv', 'w').close()
        f  = open('foo.csv','rw+')
    else:
        states = {}

    board = Board()

# attach it to a MinMax tree generator/evaluator, max depth 6:
    mm = MinMax(6)

    #sys.stdout.write("Who's first? (H)uman or (C)omputer? ")
    #sys.stdout.flush()
    #first = sys.stdin.readline().strip().lower()[0]
    first = random.choice(['h','c'])
    if first == 'h':
        curplayer = Board.O   # human
    else:
        curplayer = Board.X   # computer

    done = False

    #sys.stdout.write("%s\n" % board)

    while not done:
        if board.full(): #DRAW
            done = True
        # print all_state
            write_to_file()
            #sys.stdout.write("Tie game!\n")
            continue

        if curplayer == Board.X:
            #sys.stdout.write("Computer is thinking...\n")

        # run the minmax tree for the current board
            move = mm.buildtree(board, curplayer)

            #sys.stdout.write("Computer's move: %s\n" % move)

        else:
            badMove = True
            while badMove:
                #sys.stdout.write("Enter a move: ");
                sys.stdout.flush();
                #move = int(sys.stdin.readline())
                move = random.choice([0,1,2,3,4,5,6,7,8])
                badMove = move < 0 or move > 8 or board[move] != Board.NONE

        if move >= 0:
            board.move(curplayer, move)
            #sys.stdout.write("%s\n" % board)
            winner = board.getWinner()
            if winner == Board.X:
                write_to_file()
             #   sys.stdout.write("X wins!\n")
                done = True
            elif winner == Board.O:
                write_to_file()
              #  sys.stdout.write("O wins!\n")
                done = True

    # switch to other player:

        if curplayer == Board.X:
            curplayer = Board.O
        else:
            curplayer = Board.X

if __name__ == "__main__":
    iterations = 100
    while iterations:
        main()
        iterations -= 1