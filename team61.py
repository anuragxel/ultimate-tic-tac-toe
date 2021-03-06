import random
import json
import datetime
import signal

ENFORCED_TIME = 5
heuristic_table = {"-ox--o-xo": 0, "-xoooxx-o": 0, "-ox-x-oxo": 0, "xo-ooxx--": 7, "oxox-----": 4, "----xx-oo": 6, "ox--xooox": 3, "xx-o-ooxo": 2, "-xo-xoo--": 8, "-oxxo-o-x": 5, "-x--ooxo-": 3, "oox-o--xx": 5, "oxooxox-x": 7, "x--ooxxoo": 1, "oxx-o----": 8, "--x-o-x-o": 0, "xo--xooxo": 2, "o-xoo--xx": 6, "-ooxoox-x": 0, "-xxoo-xo-": 5, "----xoxoo": 2, "----x---o": 3, "oxx-xoo--": 7, "-x-oxo-ox": 6, "xox-x--oo": 6, "x--o-o---": 4, "xxo-ox-o-": 6, "-ox--o-x-": 6, "-xoooxx--": 8, "oox-o--x-": 8, "-x--ooxox": 3, "oxooxox--": 7, "----o-xo-": 1, "xxox-o-o-": 6, "----ox---": 8, "-oo-x-x--": 0, "x-xo-oox-": 4, "oxo----ox": 3, "xo-o-oxx-": 4, "-x-oxo-o-": 2, "x--ooxxo-": 1, "------oox": 2, "xo--xox-o": 3, "xo--xoox-": 8, "-o---x---": 2, "-o-xo-xxo": 0, "ooxoxx---": 6, "----xoxo-": 2, "xo-oxo-xo": 2, "o--o-x-x-": 6, "oxx-xoo-o": 7, "o---xx--o": 1, "ox-x-o-xo": 4, "-ox--o---": 3, "-o-x-o---": 2, "-o-oxo-x-": 6, "o-xx-ooxo": 4, "-oo----xx": 6, "xoo--xo-x": 4, "---oxo---": 8, "-xo--xxoo": 3, "-x-o--oox": 0, "oo--x--x-": 2, "---x-o--o": 2, "x-xxoo--o": 1, "-o-xxoxoo": 0, "x-xo-ox-o": 1, "o--xo-oxx": 2, "ooxoox-x-": 8, "oxoo---xx": 4, "o-----xox": 2, "o-ox----x": 1, "xoxxxo-oo": 6, "xox-ooox-": 3, "xo-xxo-o-": 8, "---oxo--x": 7, "ox--x-xoo": 2, "oo-oxoxx-": 8, "-o-ox-oxx": 0, "--xoo--ox": 5, "x-oxox-o-": 6, "-x--xo-o-": 0, "-o-oxo-xx": 6, "-ox--o--x": 6, "oo--x--xo": 2, "--oxo-x--": 8, "-xo---x-o": 5, "-oo----x-": 0, "xoxo-ox--": 4, "---x-o---": 7, "-o-xxoxo-": 2, "xox-oooxx": 3, "o-o-xxoox": 3, "o--x-o-ox": 1, "o-----xo-": 1, "xooo-x-xo": 4, "o---xxxoo": 1, "oxo-xxo--": 3, "ooxx-oxox": 4, "----oxxo-": 1, "xo-o-----": 4, "-x-oo-x--": 5, "--oxx-o-o": 5, "--oooxxx-": 8, "--ooxo-x-": 8, "-xooxoxox": 0, "xoxoxo-xo": 6, "-o--x-x-o": 3, "xx---ooox": 3, "ox-x--xoo": 4, "-o-xoooxx": 2, "-xx-o-oxo": 0, "ox-x-oo-x": 7, "xo-oxo-x-": 2, "x--xoo---": 6, "-oxoo-oxx": 5, "-x-ox--oo": 6, "x-ooxxo--": 8, "oxx---oxo": 4, "o-x---ox-": 3, "ooxx-x-o-": 4, "---x-ox-o": 0, "ooxoxo-x-": 6, "xo-o-o-xx": 6, "-o-----xo": 0, "-x--o----": 2, "-xooxoxo-": 8, "--oxx-o--": 0, "xo-xxooo-": 8, "x-ox-oo-x": 4, "oxo-o-xx-": 8, "oox-x--ox": 6, "-o-x-o-ox": 4, "-o-x-oxxo": 2, "-----oxo-": 0, "xo-x-oox-": 8, "--o--xoox": 4, "-oooox-xx": 6, "x--xoo--o": 6, "ox-xoox--": 8, "x---xo--o": 2, "oxooo-xx-": 8, "-x-ox--o-": 0, "x-ooxxo-o": 7, "--xoxxoo-": 8, "x-o-ox-xo": 6, "-x---x-oo": 6, "---xooo-x": 2, "-xxxo-oo-": 8, "---oox-ox": 2, "xo-o-x---": 8, "oox--o-xx": 6, "ox--oxo-x": 2, "-x-x-oo--": 2, "oxx--o--o": 4, "--xooxx-o": 0, "ooxx-xoxo": 4, "oxooxo--x": 7, "o--xxo-o-": 2, "-x-oxo---": 0, "x-o-oox-x": 7, "oxo-oxxo-": 8, "o---x-xo-": 3, "o---x--ox": 5, "-x-xo-oox": 2, "---xo----": 0, "--o--x-ox": 4, "-o-xxo-xo": 2, "oxxxxoo-o": 7, "-oox---x-": 0, "--xox-oxo": 1, "-xo--o--x": 4, "oxoox-xo-": 5, "xo------o": 6, "-ooooxx-x": 7, "oox--o-x-": 6, "xo-o-x--o": 7, "oxoxxo-o-": 8, "xxo-o----": 6, "ooxox---x": 6, "oxooxxxo-": 8, "o--xoo-xx": 6, "-xo-xoo-x": 7, "x-o-oxxo-": 3, "oxoxoo-xx": 6, "oxx--o---": 4, "-xoo--oxx": 4, "o---x-xoo": 3, "o-oo-xxx-": 8, "--oxoxxo-": 0, "oxoox-xox": 5, "xoo-oo-xx": 6, "oxo-oxxox": 3, "x-x-oxo-o": 1, "ooxxx---o": 7, "---xxo-o-": 0, "ooxoxx--o": 6, "xo-------": 4, "-xxo--oox": 5, "xox-xoo-o": 7, "xoxooxo--": 8, "---x-oox-": 4, "-x-o-----": 4, "x-xoo--xo": 1, "xx-oox-o-": 2, "-ox-xo-xo": 6, "-o----ox-": 2, "oxox-x-o-": 4, "---o---ox": 2, "xo-x--o--": 4, "-o-xoox--": 7, "xox-o--xo": 5, "-xxo-o---": 0, "xo--xoxo-": 2, "--ox--xoo": 0, "x---xooxo": 1, "x-x---o-o": 1, "xox-o----": 7, "o-oxo--xx": 6, "x-ooo-x--": 5, "-o----oxx": 2, "xox-xoo--": 8, "x-oxx-oo-": 8, "ox-oxx--o": 6, "xx-oox-oo": 2, "oxox-o-ox": 4, "oxx--o-xo": 4, "xoxo-xxoo": 4, "-x-xooox-": 2, "-o-xoox-x": 7, "---ox-oox": 0, "-xx-oo-xo": 0, "x-x--ooxo": 1, "o---x-oxo": 1, "--xoxx-oo": 6, "oox--o--x": 6, "oox-oxx--": 8, "-xxo-o--o": 0, "--ox--xo-": 5, "x-o-ox---": 6, "xox-o---o": 7, "-o--oxoxx": 2, "---ooxx-o": 0, "--o---xo-": 1, "-xxoxoo--": 7, "oo-o--x-x": 7, "xx-ooxo--": 2, "ox----oox": 3, "-o-x-xxoo": 0, "-o--o-xxo": 0, "xo-ooxox-": 2, "xox-oox-o": 3, "xoxox-oo-": 8, "xo-ox--xo": 5, "-oxox----": 5, "o--xoxoox": 2, "-xxoo-xoo": 0, "o-xx-oo-x": 7, "ox-ox----": 6, "oox-xo---": 6, "ox-oo-x-x": 7, "x--x-o-o-": 6, "oxx-x-o-o": 7, "oox-ox-x-": 8, "-xoo---ox": 4, "ox-xo-oox": 2, "-xxoxoo-o": 7, "o-x-ooxx-": 8, "-xoox-oox": 0, "ox--o--ox": 5, "-o--o-xx-": 0, "oxxooxxo-": 8, "--o---xox": 0, "x---xoxoo": 2, "x-o----ox": 4, "x--oxo-xo": 1, "x-x-xo-oo": 6, "o-xx-oo--": 8, "xx-o-oo-x": 4, "o-xxxo--o": 1, "-oxox---o": 6, "-ooxxo--x": 0, "oxxoo-xox": 5, "--o-x----": 7, "ox-ox---o": 7, "oox-xo-x-": 6, "o-xxooo-x": 1, "--xox-o--": 0, "-xx-o-xoo": 0, "x-o--xo--": 4, "oo--xoxx-": 8, "-xx--o--o": 6, "ox-o-x---": 6, "ox-xxo-o-": 6, "----xoo--": 8, "o-xxoxo--": 8, "-xx-ooxoo": 0, "x-x-xooo-": 1, "xoo---x--": 5, "xox---oxo": 4, "xo-o--xxo": 2, "xx-xoooox": 2, "--o-oxxox": 1, "o-xooxxo-": 8, "--oo-xx-o": 4, "x-o-o--x-": 6, "xox-oo-x-": 3, "xo-oxx--o": 7, "xooo-xx-o": 7, "oox-x-oox": 5, "x--ooxox-": 2, "--o-xx-oo": 3, "--oxx-xoo": 5, "-oxxo----": 7, "oox-xo-xo": 6, "xoxoox-xo": 6, "-xooox-x-": 6, "xoxoxx-oo": 6, "oo-oxxxxo": 2, "o-xo--xox": 4, "xooxxoox-": 8, "-oxox-o-x": 0, "-o-x--o-x": 4, "oo-x---x-": 2, "x-oo-xoox": 4, "ooxo---x-": 6, "-oxo-x-xo": 0, "xo-xxo-oo": 6, "x-ooxo-x-": 8, "oo-o-xxx-": 8, "--oo-xx--": 8, "o-x----ox": 6, "xoooox-xx": 6, "x--ooxoxo": 2, "x-o-x-o--": 7, "--o-xx-o-": 0, "xx-xoooo-": 2, "x--oxxoo-": 8, "-o--oox-x": 7, "ox-ox-x-o": 5, "--ooxx-o-": 0, "x-ooox--x": 6, "---xo-x-o": 0, "--xoxo-xo": 6, "xx-oxooo-": 2, "x-xo---o-": 4, "--o----x-": 8, "--o-x-ox-": 0, "---ox--xo": 1, "x-xoo----": 5, "oxox-ooxx": 4, "-oxooxx--": 8, "oo--o-xx-": 8, "x-ox-x-oo": 6, "xo--xoxoo": 3, "x--o---o-": 2, "-o-ox-xo-": 8, "oo-ox-xx-": 8, "xx--o---o": 6, "xoxoo--xo": 5, "xoooxxxo-": 8, "ooxx-ox--": 4, "o-o--xx--": 1, "xxoxoo---": 6, "-xox---o-": 6, "oo-xx--ox": 2, "oo-x----x": 2, "oxoxo---x": 6, "---xo--xo": 0, "x-----oxo": 1, "--o-x-oxo": 1, "x-xo---oo": 6, "x-xooxo-o": 1, "-o--xoo-x": 0, "-xo--oxo-": 8, "-oox-o--x": 0, "x-ooox---": 6, "--ooxx-ox": 0, "x-xoo---o": 1, "xx-oo-oox": 2, "--oooxxox": 1, "xx-o-oxo-": 4, "ox-x-o---": 7, "--o-xo-x-": 8, "--o--o--x": 6, "oo-ox-xxo": 2, "x-x-ooxo-": 1, "x----o-xo": 2, "xxoo-xo--": 4, "-o-ox-xox": 2, "ox---o-ox": 4, "xox--o-o-": 4, "o-o-oxxx-": 8, "-oo-xx-o-": 3, "xoo--oxox": 3, "ox-----ox": 3, "xoo-o--xx": 6, "x-x-ooo-x": 1, "xoxoo-xxo": 5, "-x-o-x--o": 0, "xooox-xxo": 5, "x-ooox-x-": 6, "-xo-x-o-o": 7, "xx-oxo-oo": 2, "--x--o-xo": 3, "-xoox--ox": 0, "oo--xxo--": 3, "-xo-oxxo-": 8, "oxo-xxo-o": 7, "xo-o--ox-": 5, "-ooo-xx-x": 7, "oxo-xxxoo": 3, "--x-ooo-x": 3, "xooxox---": 6, "-x--oxo--": 2, "xox-ox--o": 7, "xxo--ooox": 4, "ox-x----o": 4, "oo----xx-": 2, "-xox-o---": 8, "xxoox---o": 7, "-o---xx-o": 4, "xo-xo--xo": 6, "-oo-xx-ox": 0, "ox-----o-": 6, "x----ox-o": 2, "x-xo-o-o-": 1, "-x-oxooox": 0, "xx-oxo-o-": 8, "-xo-x-o--": 5, "xoo-o--x-": 6, "o-o-o-x-x": 7, "-oxo-x---": 8, "--o--oxox": 0, "o--x-xxoo": 4, "--xoox-o-": 8, "-xooxoo-x": 7, "xooxox--o": 6, "o-o----xx": 1, "oo--xxo-x": 3, "---o--xxo": 4, "o-ox-xoox": 4, "x-o--xoxo": 4, "o-xxoo--x": 1, "--oox--xo": 1, "o---o---x": 6, "ooxx--oxo": 4, "xoo-xxo--": 8, "--x--o---": 4, "-o-xo--x-": 6, "-oxoxxoxo": 0, "xoo-x----": 3, "--ox-oxox": 0, "xoooo--xx": 6, "x--oo-x-o": 5, "o-ooxxx-o": 1, "--xx--oo-": 8, "x--ox-o-o": 7, "-xxxooxoo": 0, "--oxx--o-": 0, "x-xoxo--o": 7, "x---o--o-": 1, "---ooxoxx": 2, "o-x-xxo-o": 3, "ox--x-o-o": 7, "oxxo--xo-": 5, "-oxoxooxx": 0, "-o----x--": 4, "--x---xoo": 0, "xx-o----o": 4, "--oox--x-": 6, "oxx--oxo-": 4, "oxo--xx-o": 4, "o-xxoo---": 8, "--x--o--o": 0, "o-xoo---x": 5, "xo-ox-xo-": 5, "-oo--x-x-": 0, "o--oxx-o-": 6, "oxoox--ox": 6, "xxooo-x--": 5, "xoo-x---o": 5, "x--oo-x--": 5, "o-ooxxx--": 1, "o--o-xxxo": 4, "x---o--ox": 1, "xx-oxo--o": 7, "x--ox-o--": 7, "oox-xxoxo": 3, "o-o-x--ox": 1, "-oxoxoox-": 0, "-oo-xxx-o": 3, "xo--x-oo-": 8, "oxxo--xoo": 4, "ox-x-xoo-": 8, "-o---xo-x": 4, "-ooxx-o-x": 0, "xoox-oo-x": 4, "oox-x-ox-": 3, "-oxo---x-": 6, "oo-xxo-x-": 2, "-o-x-ox--": 2, "xo-oxox-o": 2, "ooxxo--x-": 8, "x-xo-o---": 1, "xoo--xoxo": 4, "-ox-o-o-x": 5, "oxox-xoox": 4, "xox--ox-o": 4, "oox-x----": 3, "---xx-o-o": 5, "o-x-xo-ox": 6, "--o-ox-x-": 6, "x-xx-ooo-": 8, "---o--x-o": 5, "xx--oo-ox": 2, "x--oxox-o": 2, "-ox-o-ox-": 8, "-o-x-o--x": 0, "x-oox-oxo": 1, "ooxo-x-x-": 8, "-ooxx-o--": 5, "-o-o--xox": 4, "o---o--xx": 5, "-oo-o-xx-": 0, "-oo-xoxx-": 8, "xo---xoxo": 4, "-oxo---xo": 0, "oox-x-oxo": 3, "x-xo-o-xo": 1, "--xo--ox-": 0, "xo-oxox--": 8, "x-oox-xoo": 5, "o--x--x-o": 4, "xoo--xox-": 4, "-ox-o-oxx": 5, "-xooo-xox": 5, "---o-xo--": 0, "o--o-xxo-": 2, "o-xox----": 6, "x-oox-ox-": 1, "---ooxx--": 8, "--o-x--o-": 6, "----xoo-x": 0, "-x-ox-oox": 0, "-xoo-ox-x": 7, "xx--oox-o": 3, "o-oxo-x-x": 7, "ooxo--x-x": 5, "-oxxooox-": 0, "xx--ox-oo": 2, "xx--oo-o-": 3, "oox--oxox": 4, "-oxx-oox-": 0, "x-xoo-xoo": 1, "xox-oo-xo": 3, "o-xx-o--o": 4, "x-oo-xoxo": 4, "-oxx-oo--": 4, "-o-xx-oox": 0, "-o--x---o": 0, "---o-x-xo": 0, "xoxo-xo--": 8, "--x-----o": 1, "x--o-ox--": 4, "ox-x-x-oo": 4, "-oxox-o--": 0, "-x--xooo-": 8, "xxo-o-x-o": 3, "-ooxx-ox-": 0, "xoooox-x-": 6, "-oxxoooxx": 0, "ox-oox-ox": 2, "--xo--o-x": 5, "o-xooxx--": 8, "--o-x--ox": 5, "-o--xx--o": 3, "o-xxx-oo-": 5, "-oxx-ooxo": 4, "x-xx-oo-o": 1, "x-xoo-xo-": 1, "ox-xo----": 8, "o-xx-o---": 8, "ooxooxx--": 8, "oo-xo--xx": 6, "x-----oox": 5, "-oxoo---x": 5, "-o--x----": 6, "-x--xooox": 0, "-o-xx-oo-": 5, "-oxx-oo-x": 4, "--o-o-xx-": 0, "-oxx-xoo-": 8, "-ooxx-oxo": 5, "--ooxx-xo": 1, "-xx--oo-o": 0, "x-ooxoxo-": 8, "x-ooo--xx": 6, "o-o-xx--o": 1, "-ox--xoxo": 4, "oo--xxx-o": 3, "o--x-oxox": 2, "--o-xo-ox": 0, "xoxox--o-": 8, "x-xo-oo-x": 1, "xo-ooxo-x": 2, "xo-xooox-": 2, "oxo-xox--": 7, "--ox--o-x": 4, "xo---oxox": 4, "x-xxoooxo": 1, "o-----xxo": 4, "-o-x-xoox": 2, "--oo-x-x-": 1, "oxx--ox-o": 4, "-oxoxxoo-": 8, "-o--x-oox": 2, "-------xo": 0, "-xooxx--o": 7, "---xo--ox": 1, "o-xx--xoo": 4, "-xx-o-o--": 0, "o-oxo-xx-": 8, "---------": 6, "-o-xooxxo": 0, "--o-x-oox": 0, "-o-ox-xxo": 2, "-xx--oo--": 7, "xo-o-xox-": 8, "-o-oxxx-o": 2, "o-o-xx---": 1, "-oxoxxo--": 8, "-xoox--o-": 8, "ox----o-x": 3, "xoxox--oo": 6, "x-xoxooxo": 1, "-o--xooxx": 0, "-o-oxoxox": 2, "-xxoo----": 0, "o-oxxo--x": 1, "o---x--xo": 6, "xoxo-oo-x": 4, "xx-oo-ox-": 2, "o-x-xo-o-": 6, "ooxx-xo--": 7, "o--oxx-ox": 2, "xo---oxo-": 4, "-oxoxo-ox": 0, "o--xox-ox": 2, "--------o": 4, "-o-xooxx-": 8, "-xx---o-o": 7, "--ooxo--x": 0, "xoox-x-oo": 4, "-xo-o---x": 6, "ooxxxo-o-": 6, "ooxo-xx-o": 4, "o-ooxox-x": 7, "ooxxoxox-": 8, "o--x-ooxx": 1, "o---xxo-o": 3, "xoo-x-xoo": 3, "o-x--x--o": 4, "x--oox-o-": 1, "xxooxoo--": 7, "xoox--o--": 4, "---o-xo-x": 0, "-x-ooxoox": 2, "xoo----x-": 3, "o---oxx--": 8, "oox-oo-xx": 6, "-xx----oo": 0, "-o-oxx-o-": 8, "-oxox--xo": 6, "-x--o-x-o": 0, "-xox-ooox": 4, "---oxx-o-": 2, "-xx--ooxo": 4, "-x-xoooox": 2, "-ooxxox--": 0, "-oxx-o-xo": 6, "xoox-x-o-": 4, "ooxo-xx--": 8, "o-x-oo--x": 3, "---o---x-": 4, "-x-oo---x": 5, "-xxoo--xo": 0, "----x-xoo": 0, "o---xxo--": 3, "-xo-ooxox": 3, "---xxooox": 0, "xx--o-o--": 2, "-xox-oxo-": 0, "o-oooxxx-": 8, "-ooox-xox": 0, "oxxxooo-x": 7, "xx-o-o-ox": 4, "xox-o-o-x": 5, "oxoo-xxxo": 4, "xoo----xo": 5, "xoox--o-x": 4, "x--oox-ox": 2, "------xo-": 4, "xoooxx--o": 7, "o----x-xo": 4, "x-xo--oox": 4, "--xo---ox": 5, "xoxx-o-o-": 6, "----xoox-": 1, "xox-x-oo-": 8, "-o-oo--xx": 6, "oxo-x--o-": 8, "-x-x-ooox": 0, "-xxxooo-o": 0, "x-x-o---o": 1, "----o-oxx": 2, "oxxoxo-o-": 6, "xxo-x-oo-": 8, "x-xo-xo-o": 1, "---oxoxo-": 0, "-oo-x--ox": 0, "ox-xx-o-o": 5, "x-xo--oo-": 8, "xoooxx---": 8, "o-xx--o--": 5, "o---ox-x-": 8, "x-o-oo-xx": 6, "xo--oxox-": 2, "xo-xxooxo": 2, "--x---oxo": 1, "-x----o--": 0, "----xooxo": 1, "oox----ox": 4, "oxxoxo-ox": 6, "x-oxoo-ox": 6, "ox-x---o-": 8, "---oxoxox": 2, "-xxxooo--": 0, "-oxo-oxx-": 4, "oox-oox-x": 7, "xxooox--o": 6, "ox-x-oxo-": 2, "--x-x-o-o": 7, "ox-xxoo-o": 7, "x-xo-oxo-": 4, "x--xoo-o-": 6, "xoxoxxoo-": 8, "x--oxooxo": 1, "-o--oxx--": 7, "xox-o-ox-": 5, "xo--oox--": 3, "-oxxxoo-o": 7, "-oxo-xxo-": 8, "xoxx-ooox": 4, "xoxo--oox": 4, "ooxxoxo--": 8, "xooxxoo--": 8, "oxo-xo---": 7, "o-xxo-o-x": 5, "x--oo--x-": 5, "ox-xxo--o": 2, "x-ox--o--": 4, "-xo--oxox": 0, "xoxo-o-xo": 4, "x-o--oxo-": 3, "o-xxxoo--": 7, "x--oo---x": 5, "-xxo-oxo-": 4, "-o-x--xo-": 0, "-xo--x--o": 4, "x-xo-oxoo": 1, "ox-xxoo--": 7, "x--oxoox-": 1, "-o-oox-xx": 2, "ooxx-oxxo": 4, "oxx---oox": 5, "xx-x-ooo-": 8, "oo-xxoxox": 2, "xox-o-oxo": 5, "-oxxxoo--": 0, "-xo--xoox": 4, "xx-o-o---": 4, "xoxxo-oxo": 5, "x--oo----": 5, "xx-----oo": 6, "-oxxxo--o": 6, "x----x-oo": 6, "x---o-o-x": 2, "--oxooxox": 0, "x-xoo-ox-": 1, "xooxx-oo-": 5, "oxo-xo--x": 7, "--oox--ox": 0, "oxo-xx--o": 6, "-o-x--xoo": 0, "x-o--oxox": 4, "x----o---": 2, "xoxoxo---": 6, "-xx-oo-ox": 0, "-xoxoxxoo": 0, "xo-oxo---": 6, "-o-oxooxx": 0, "xo--o--xo": 6, "x--oox-xo": 6, "oo--x-x--": 2, "---ox-x-o": 1, "--o-o-xox": 1, "--oxo-xxo": 0, "---ox---o": 6, "-xooo--xx": 6, "-x-x--oo-": 8, "-ox---o--": 8, "-oxxoox-o": 0, "o--ox-xo-": 2, "xoo--ooxx": 4, "--o-xoox-": 1, "-xo-xxoo-": 3, "--o-xxoo-": 3, "ox-o-oxox": 4, "-o--xoxo-": 3, "-xoxo-xo-": 0, "-----x--o": 0, "o---xoo-x": 3, "ooxxx-o-o": 5, "xoxoxo--o": 6, "--xx-o--o": 0, "-o-oxx-xo": 0, "-xxooxxoo": 0, "oxoooxxx-": 8, "-xx-oo-o-": 0, "-x---o---": 2, "-ooo--x-x": 7, "o-x-x--o-": 6, "-ox-----o": 4, "xo--o--x-": 6, "ox--xxo-o": 3, "----o-xxo": 0, "oxox-xxoo": 4, "ox-oo-xx-": 8, "--o-xxoox": 1, "oxxo-x-o-": 8, "oxo--x---": 4, "xooxx---o": 5, "-oxooxox-": 8, "---ox----": 8, "-oxxoox--": 0, "ooxx-o-xo": 4, "-o--xoxox": 3, "x-x--o--o": 7, "xooxox-xo": 6, "-xoxo-xoo": 0, "xoo-xox--": 3, "-ox---o-x": 4, "ooxxx-o--": 5, "---o-o--x": 4, "oo-x-xoox": 2, "xx-xo--oo": 6, "-o-x-xoxo": 4, "xo----xoo": 4, "o-oox-xxo": 1, "xoxoox--o": 7, "xxo--oox-": 4, "-o--xxo--": 3, "oo--xo--x": 2, "-xoxoo--x": 6, "xooox-x--": 8, "o-xoxo-ox": 6, "o--ox---x": 6, "x--o-x--o": 4, "-o-o-x-x-": 8, "-o---ox-x": 4, "xoo-x-oxo": 5, "-ox-x-o--": 5, "xx--ooo-x": 2, "xx--o-oxo": 2, "-xoo-x---": 6, "o--xxooxo": 1, "----xxo-o": 7, "-x---oxoo": 2, "oxx-oo--x": 3, "-x--oxxoo": 0, "xo----xo-": 4, "o-oox-xx-": 1, "--ooo-x-x": 7, "x-o-xoxo-": 8, "xoxoox---": 8, "-oxx--oxo": 0, "-o--x-o-x": 0, "-o--xxo-o": 3, "oo----x-x": 7, "-o-----ox": 4, "-oo-xxoox": 3, "--oo-ox-x": 7, "o-x-oxox-": 8, "x-x-ooox-": 1, "-x-x-o--o": 2, "x-o-x-oxo": 1, "o-xo----x": 6, "xoo-x-ox-": 3, "oxoxx-oox": 5, "-ox-x-o-o": 7, "o-oxoox-x": 7, "o--xxoox-": 1, "ox-oxxxoo": 2, "o--ox----": 6, "-x---oxo-": 2, "--ox-----": 0, "o--oxxx-o": 7, "--o--o-xx": 3, "ooxxooxx-": 8, "o-xx-oxo-": 4, "ooxxxo-ox": 6, "x-oooxxo-": 1, "--x-xoo--": 1, "oxo--ooxx": 4, "xoxxxoo-o": 7, "x-ox---o-": 6, "-xoox-xoo": 5, "--xo-o---": 4, "-xoo-xxo-": 8, "xoooxxo--": 8, "----oox-x": 3, "-xo-o-xox": 3, "xooo--x--": 8, "xoo-x-xo-": 8, "xoo--xx-o": 3, "o--ox-xxo": 1, "ox--o-x--": 8, "oxxxoo---": 8, "o--o-xx-o": 4, "---x--oox": 5, "-ox--x--o": 4, "--x-xooxo": 1, "o-xx-oxoo": 4, "--xo-o--x": 4, "--x-xoo-o": 7, "xoxx-o--o": 6, "o--ox-xox": 2, "-xo-o-xo-": 5, "-xoox-xo-": 5, "xooo--x-x": 5, "-xoo-xxoo": 0, "oo---ox-x": 2, "o--oox-xx": 6, "-o-oxx-ox": 2, "xooo--xx-": 8, "ox-o--x--": 8, "o-oxx--o-": 5, "-o---x-xo": 2, "oo-ox-xox": 2, "ox--xx-oo": 3, "xooxo----": 6, "-oox-x-xo": 0, "-x--o-oox": 2, "xo-o-ox--": 4, "o-xo-xxoo": 4, "o--xxooox": 2, "--xxooxo-": 0, "--xoxoo--": 0, "oxoxxo-ox": 6, "o-ox-o--x": 1, "--x-o-ox-": 8, "-x-xo--o-": 0, "-xo--ooxx": 4, "xoxo--oxo": 4, "xoox---o-": 4, "o-xox--xo": 1, "o-oxx--ox": 5, "xoox-ooxx": 4, "xx--o-oo-": 2, "o-x-x-o--": 3, "--ooxoxx-": 8, "xxoo--o-x": 4, "o-xo-xxo-": 1, "-o-xx--oo": 6, "-xx-xoo-o": 0, "xoo-xx-oo": 3, "oo--xoxox": 2, "o-ox-o-xx": 1, "--xoxoo-x": 0, "o--oxo--x": 6, "xoxo--ox-": 8, "xo-ox-o--": 8, "oxoxx--oo": 5, "x-o---xo-": 8, "oo-xx--o-": 2, "o--xxoo--": 1, "xo-x-xo-o": 4, "xooo-xoxx": 4, "o--ooxxox": 2, "ooxo--xx-": 4, "-x-o-xoox": 2, "oxo-x-o-x": 3, "-oooxo-xx": 6, "x-x--oo--": 1, "x-xox-o-o": 1, "-ox-xooox": 0, "-xoo--xo-": 4, "xx-oxoxoo": 2, "ox--xoo-x": 7, "x-o-o-xo-": 3, "--x-o---o": 0, "-oxxoo--x": 7, "-ooo-xx--": 0, "xo-oxxo--": 8, "xx-o-ooox": 4, "o-o-xxx-o": 1, "xox-----o": 6, "-xx--o-o-": 4, "o--xo--x-": 8, "x-o---xoo": 3, "x--ooxoox": 2, "oxo-x-o--": 3, "xoo-xoxo-": 8, "-xo---xo-": 8, "-ooo-x-xx": 6, "o---o-xox": 1, "oxoxoxxo-": 8, "ooxo--xxo": 4, "o-x-x-oxo": 1, "x-x--oo-o": 1, "------xoo": 3, "xooo-xox-": 4, "oo-oxx-ox": 2, "o-x-xooox": 3, "--oox-ox-": 0, "--oxoo-xx": 6, "--x-o----": 1, "---xoo-ox": 1, "-xoo--xox": 5, "---oxo-x-": 0, "oo-xx-oox": 5, "xxooxxo-o": 7, "oox-o-xx-": 8, "xo-oxxo-o": 7, "xo-o-xx-o": 4, "oxoo--xx-": 4, "-o-x---xo": 0, "o----x-ox": 4, "x-o-o-xox": 3, "xooo-ox-x": 4, "xx--o-xoo": 5, "oo-----xx": 6, "xxoox-o-o": 7, "o----xoox": 3, "-oxo--oxx": 0, "x--oxo---": 8, "-o-ox----": 2, "x---o-x-o": 1, "xo-x-oo-x": 4, "x-xxooo-o": 1, "oxx-----o": 4, "ooxox--xo": 6, "--ooox--x": 6, "--xooxox-": 0, "x-oxxoo--": 8, "--xoo-o-x": 5, "oo---x-x-": 2, "oo-xxoox-": 2, "-xxo----o": 6, "-x-xoox-o": 0, "-o-----x-": 8, "-o--xo-x-": 8, "-xxxo--oo": 0, "-o-ox---x": 6, "-oxoxo-xo": 6, "-oxo--ox-": 0, "---oxxoox": 0, "xxoox-o--": 5, "x--oxo--o": 2, "----xo-ox": 6, "xxooxoxo-": 8, "oo-----x-": 2, "-oxx-o---": 6, "x-oox--o-": 8, "ooxox--x-": 6, "xx-ooxoxo": 2, "xxoooxx-o": 7, "-ox-xoox-": 8, "----oxoox": 2, "-o-xo---x": 7, "xox-xooxo": 3, "oxx-ox-o-": 8, "-xo------": 6, "ox--oo-xx": 6, "oox--x-o-": 4, "x-oxox--o": 6, "--x--oo-x": 0, "ox---ox--": 4, "----o-x--": 5, "x---x-o-o": 7, "xoxoo-o-x": 5, "ox--xoxo-": 2, "-o-xxo--o": 2, "-xxoxo-o-": 0, "x--oxoxoo": 2, "xx----oo-": 8, "o-o-xoxx-": 1, "xoox-o-ox": 6, "--oo--x--": 4, "-oo-xxoxo": 3, "-o--x-oxo": 0, "xo-oxxxoo": 2, "o---xxoxo": 3, "--xoxo-o-": 6, "ooxx--ox-": 5, "--oxx--oo": 5, "x-ooxx-o-": 8, "oox-ox---": 8, "ox--xo---": 7, "ox--xoo--": 7, "-xox-oo-x": 4, "xo-o--x--": 8, "--x-ox-o-": 1, "oxo---x--": 7, "----o-x-o": 0, "--oo--x-x": 0, "xo-ooxoxx": 2, "x---oxoox": 2, "-o-xxo---": 0, "-xxoxo-oo": 0, "--x--oo--": 4, "x--oxoxo-": 8, "o-xoxx-o-": 8, "-xoxo--ox": 6, "---o-xox-": 0, "--o-oxx--": 0, "----ox-ox": 2, "xox--oxoo": 4, "-ox-xo---": 0, "-oo-xxox-": 0, "ox----xo-": 2, "-o--x-ox-": 5, "o-x-oox-x": 7, "xx-ox-o-o": 2, "-o-x--ox-": 0, "-xx-ooxo-": 0, "-oxo--o-x": 5, "xoo---x-o": 3, "x-ooxx-oo": 6, "-xo-xo---": 7, "--xoxo-ox": 6, "xo-o--x-o": 4, "--oxxoo--": 8, "-ox-ooxx-": 8, "------ox-": 0, "-oxx-oxoo": 4, "o--xx-xoo": 1, "xo--x---o": 3, "xxoo--o--": 4, "o-o--o-xx": 6, "xx--o-oox": 2, "x---oxxoo": 3, "oo-xxoo-x": 2, "-xx--o-oo": 0, "--oox-xxo": 1, "xxo----o-": 6, "x--xoo-ox": 1, "oo-ooxx-x": 7, "-oxoo-xx-": 8, "--o--xo-x": 4, "oox-xxoo-": 8, "-x--xo--o": 7, "oo--x--ox": 2, "-oox-xxo-": 4, "-o--ox-x-": 8, "oox-x---o": 3, "x--ox---o": 2, "-oxx-oxo-": 0, "oxx-o-o-x": 5, "--oxxoo-x": 7, "-x-oxx-oo": 6, "x-ooxxoo-": 8, "-o--xoox-": 0, "-xoxxo-o-": 8, "xoxooxox-": 8, "o-x-o--x-": 8, "xoooo-xx-": 8, "x-xo-oo--": 4, "oo-x-xx-o": 4, "xx-oxoo--": 2, "-oxxoo---": 7, "--xo-oxox": 4, "--oxx-oo-": 5, "oxo-----x": 7, "xx--xo-oo": 2, "o---xoxox": 2, "-ooxx----": 5, "xxooox-o-": 6, "-o-oxxoxo": 0, "oxxx-o--o": 4, "-xoxxoo--": 8, "o-xo-x---": 6, "x-xxooo--": 1, "--xxooo--": 7, "oxx-o--ox": 5, "x-----xoo": 4, "-ox-o----": 7, "-oxx-o--o": 6, "o-o-oxx-x": 7, "oxx-xooox": 3, "-ox-xooxo": 0, "o---xoxo-": 2, "o-oooxx-x": 7, "--xooxxo-": 8, "xxooox-ox": 6, "oxxo---ox": 6, "x--oxx-oo": 6, "-ooxx---o": 5, "--oxx-oox": 0, "x-ox-o---": 8, "x-oo-ox-x": 7, "-x---xoo-": 8, "--o-xooxx": 3, "-ox-o---x": 5, "oxox-oo-x": 4, "-x-ox---o": 2, "oxx-o--o-": 8, "--xxooo-x": 7, "oo--x---x": 2, "xo-xo----": 6, "o-xo-ox-x": 7, "--o-x--xo": 5, "xoxo--x-o": 4, "o-xo-oxx-": 4, "o--o-xx--": 2, "xoox---xo": 5, "--xxo-xoo": 0, "xoo--x---": 3, "oo-o-xx-x": 7, "xxoo--oox": 4, "o--o--x-x": 1, "x-o-o-xxo": 3, "---x-o-ox": 0, "o-ox-xo-x": 4, "xxo-o--o-": 6, "ox--xoxoo": 2, "---oxo-ox": 2, "oxo--oxx-": 4, "oxo-xoxo-": 8, "o--x-o--x": 7, "oxxxxooo-": 8, "----x--o-": 8, "---oxxxoo": 2, "xxo---oxo": 4, "xoo-oxx--": 7, "x--xo-oxo": 2, "o--x-o-x-": 4, "x--xo--o-": 6, "x--o-xxoo": 2, "-xo-x--o-": 5, "oo-x-xo-x": 2, "x-o-oxx-o": 3, "x-ooxo---": 8, "--ooxxoox": 0, "oo-xoo-xx": 6, "o--x-----": 2, "o--o--x--": 7, "--o-x-x-o": 5, "x--ooxx-o": 7, "o--oo-x-x": 5, "---ox-o--": 0, "o----ox-x": 4, "xxo-o--ox": 6, "-xooxxxoo": 0, "---x-o-o-": 2, "xo-oxx-oo": 6, "--xxxooo-": 8, "oox-oxox-": 8, "-x-xo-xoo": 0, "ox--oxoox": 2, "o--x-o---": 2, "-o---x-ox": 4, "-xooxo-ox": 0, "oo-o-xx--": 2, "---xxo--o": 2, "-xoo----x": 7, "xo---o---": 6, "----x-oox": 5, "o---x-ox-": 3, "x-o-ooxox": 3, "-ooxxoxo-": 0, "--o-oo-xx": 6, "oo-xx-oxo": 5, "--o-o---x": 6, "--o-----x": 6, "o---x---o": 7, "-ooox--xx": 0, "oo-xxoxo-": 2, "-x-xooo-x": 2, "xx---o-o-": 4, "ox--o---x": 5, "x-x-o-oox": 5, "x-xooxoxo": 1, "xo----o--": 4, "-xxo-oox-": 4, "-ox--ooxx": 3, "o--oox--x": 2, "oxx-xo-o-": 6, "---xxoxoo": 0, "oxxoox-o-": 8, "--o---x--": 0, "----x-oo-": 8, "x-oxx-o-o": 5, "o-x-o-o-x": 5, "oo-xx-o--": 5, "-o-xoxox-": 2, "---oo-xx-": 8, "x---xo-o-": 6, "-o-xxox-o": 0, "xo----o-x": 4, "xxooxo---": 7, "--ox--x-o": 0, "xx---ooxo": 4, "o-x-o-oxx": 5, "----oxx-o": 0, "----x--oo": 6, "-x-oo-xo-": 5, "xo-xxo--o": 6, "xoox-----": 6, "oxx-xo-oo": 6, "-ooox--x-": 0, "--oo---xx": 0, "o-xoo-xx-": 8, "xx-xoo--o": 6, "--x-x--oo": 6, "xoo--o-x-": 8, "---oo-x--": 5, "oxo-oxx--": 8, "-o--x-xo-": 3, "oxox--oox": 4, "o-x------": 5, "o---xo-xo": 1, "--xx-oxoo": 4, "x---ooxxo": 3, "---xo-ox-": 2, "ooxxxo-xo": 6, "--xoxooxo": 1, "oxo-x-xoo": 5, "-oxo--xxo": 4, "xoo-oxxxo": 3, "--xo---xo": 1, "-oox-oxx-": 8, "---x-ooox": 4, "-x--o--o-": 8, "xo-x-o---": 8, "xo-o-x-o-": 4, "xoo--o-xx": 6, "xox-xo--o": 6, "xxoxo--o-": 6, "o-xo--x--": 5, "-o--x-xoo": 0, "-xo-ox---": 6, "-ox-o-xxo": 0, "-x--oo-ox": 3, "xxoo--xo-": 5, "o---xo-x-": 1, "-oo-xox-x": 0, "oxox-o-x-": 8, "-x--o--ox": 2, "--xoxoox-": 1, "x-o-xo---": 8, "oxo-x-xo-": 5, "o--xooxox": 1, "x--x-o--o": 6, "-x--x--oo": 6, "-x-oox-ox": 2, "-oxoxoo-x": 0, "o-xoo-x-x": 5, "-xoo-x-xo": 4, "o-ooxx-xo": 1, "--oxoo--x": 6, "oo-x-ox-x": 7, "-x-o---ox": 0, "--xox---o": 6, "xo--oo-xx": 6, "o-xoox-x-": 8, "-o--o--xx": 6, "--oo-xxo-": 1, "-xxo-o-ox": 0, "o-xoox---": 8, "---o-xxoo": 4, "----o---x": 2, "oox----xo": 4, "oo-xx-xo-": 2, "-o-ox-x-o": 2, "xoo-xxoxo": 3, "xx-o-xo-o": 2, "xo-x-o-xo": 6, "-o-x-----": 4, "-x-o---o-": 8, "-ox-xxoo-": 3, "-o--o--x-": 8, "xo--oo-x-": 3, "o-xx-x-oo": 4, "o-xo--xxo": 4, "ooxoo--xx": 5, "xoo-xo---": 8, "o-oxx-oox": 5, "x--o-----": 2, "oo--x-xxo": 2, "---o-xxo-": 2, "-o-ox-x--": 0, "oox----x-": 5, "x-xo--xoo": 5, "-oo-x--x-": 0, "oxxo---xo": 4, "-ooooxxx-": 8, "--o-xx--o": 1, "oo-xo-xx-": 8, "xoo---oxx": 4, "xox--o--o": 6, "x-o-x--o-": 6, "o-xxo----": 8, "xo-oxoxxo": 2, "-o--xo--x": 7, "-x-oxoo-x": 0, "-xxoxooox": 0, "-xxoo-oox": 0, "xoxox-o--": 8, "-xx-o--o-": 5, "x-x--oxoo": 4, "o-xxoox--": 8, "xo--oox-x": 7, "-xoox-o-x": 0, "--o--ooxx": 4, "-o--oo-xx": 6, "oox-xx-o-": 3, "--x-o-xo-": 1, "o-x-oo-xx": 6, "oo-x-oxx-": 8, "--o-xxxoo": 3, "-x-oxoo--": 0, "-o--xo---": 8, "o--xo-x--": 8, "x-oo--xox": 4, "x----oxo-": 3, "-o-xoxo-x": 2, "xoo---ox-": 4, "--ooxox-x": 7, "-o-x-o-x-": 6, "xoxox-o-o": 7, "--xo-xo--": 0, "ooxx-o-ox": 4, "-xx-o--oo": 0, "oox-o---x": 7, "-oxxx--oo": 6, "xoxox-oxo": 5, "-o-xx-xoo": 0, "-xx-o-oo-": 0, "---xx--oo": 5, "o-----x--": 2, "ox-o---ox": 6, "o--x---ox": 5, "-oox-xo-x": 4, "-xoxoo-ox": 6, "-xoox-o--": 7, "-oox-xox-": 4, "oxo---xxo": 4, "-x--ox--o": 0, "-----xxoo": 3, "xoxo---ox": 5, "o--xoo--x": 7, "-x-oo-xox": 5, "o---ox--x": 7, "xoo-oox-x": 7, "-x-o-x-o-": 2, "-o--x--xo": 3, "x-oo-xo-x": 4, "-o-xo-x--": 7, "--ooxo-xx": 0, "x---o---o": 2, "ooxo-x---": 8, "x-x-o-oo-": 1, "o--xxoxo-": 2, "oxxo--x-o": 4, "--xxoo---": 0, "-xxoox--o": 0, "xx-o--xoo": 2, "-ox-oxox-": 8, "xoo---xxo": 3, "xoxoxoox-": 8, "x-xo-x-oo": 6, "x-x-oooox": 1, "xoxxo-o--": 7, "x-oo-xo--": 4, "ooxo-ox-x": 7, "----o-o-x": 2, "xx-ooxxoo": 2, "oox-xo-ox": 6, "x---ox--o": 6, "--xx--o-o": 7, "o-ooxxxo-": 1, "xoxo---o-": 4, "-xx-oox-o": 0, "oxxxooo--": 8, "---o-xoox": 0, "-o---xox-": 3, "oxxox--o-": 6, "x---o----": 7, "xoxx-ooxo": 4, "-oxx--oox": 5, "oo--ox-xx": 6, "-oxxx-oo-": 8, "ooxxoox-x": 7, "-oooxx-ox": 0, "--xxoo--o": 0, "-ox-oxoxo": 0, "xo-xx-o-o": 5, "oxoxo--ox": 6, "xo-ox-ox-": 8, "--xoox-xo": 0, "x--o-xo--": 2, "---o--xo-": 4, "--oo-xxxo": 1, "xx-oo-o-x": 2, "ooxo----x": 5, "xx-o-xoo-": 2, "-oo-x-ox-": 0, "-xooo-x-x": 7, "o-o-x---x": 1, "xoooxxx-o": 7, "ox-oxox--": 7, "xo--x-oxo": 3, "oo--xxxo-": 2, "---xoox--": 7, "--oxo-xox": 0, "--x-xo--o": 0, "xoo-ooxx-": 8, "xo--x-o--": 5, "--oooxx-x": 7, "--o--xxo-": 3, "---o--xox": 4, "xo-ox-oxo": 2, "x-xooxoo-": 8, "xx-oo-o--": 2, "x------o-": 2, "-ooxxoxox": 0, "-xx-xooo-": 0, "-oxo--xox": 5, "--oooxx--": 0, "ox--x-oox": 3, "ox-oxox-o": 7, "-oo-x-oxx": 0, "---xoox-o": 0, "oo--xxxoo": 3, "xo--x-o-o": 7, "x--xxo-oo": 6, "ox-xoxoox": 2, "--xo--oox": 5, "-ox---ox-": 8, "xo-oo--xx": 5, "-xxo-xoo-": 8, "---ooxxox": 2, "o----xx-o": 4, "ox-o--xxo": 4, "o---x-o--": 3, "--xoo--x-": 5, "oxo--ox-x": 7, "--ox-xxoo": 4, "-ox--xo--": 3, "ox-ooxxo-": 8, "ox-xoooxx": 2, "o----o--x": 6, "x-o--x-o-": 4, "xox---oox": 4, "--o-x---o": 5, "xoooxoxx-": 8, "ox-x--oox": 5, "o---x-o-x": 3, "-ox--oox-": 4, "---ooxxo-": 1, "-ox---oox": 5, "-ox---oxo": 4, "---xoo-x-": 6, "xo-x--oxo": 2, "xo-oo--x-": 5, "-oo---x-x": 0, "x-o---o-x": 4, "xx--xooo-": 2, "xx-oo--o-": 2, "-x-xxoo-o": 7, "-oo-xooxx": 0, "o---oxxox": 2, "-oxxo-x-o": 0, "xxoo-----": 4, "x-----o--": 8, "ox-ooxxox": 2, "--xxooox-": 1, "oxxxoo-o-": 8, "oxo--xxoo": 4, "-oxo-ox-x": 4, "ox-oxo-ox": 6, "ox---oxxo": 4, "xoox-xo-o": 4, "--xxo-oxo": 0, "---o-ox-x": 7, "oxoox---x": 7, "-oooxxx-o": 0, "-xo-x-oo-": 8, "o-oxx-oxo": 5, "-xo-oxx-o": 0, "o-xx-o-o-": 4, "o--xx-o--": 7, "x-xoox-oo": 1, "x-x---oo-": 8, "-xooox-ox": 6, "-xx-ooo-x": 0, "-xxoo--ox": 5, "oxoox----": 7, "---o-ox--": 4, "-----o---": 2, "oxo--xxo-": 4, "-xo-x-oox": 5, "xoo-xxoo-": 3, "oxxxo-oox": 5, "--xoo-xox": 5, "----oxox-": 2, "xxo-oxxoo": 3, "xoox-xo--": 4, "oxxxoo-ox": 6, "-oooxxx--": 0, "ox---o--x": 7, "-oooxoxx-": 8, "xxo-xoo--": 8, "oxxoo--ox": 5, "--xo-x-o-": 6, "o-oxx-ox-": 5, "o--xx-o-o": 7, "x-xoox-o-": 8, "-xx--ooox": 0, "ooxo--xox": 5, "oo-oxo-xx": 6, "xx---oxoo": 3, "o-xo-oxox": 4, "-o-x-oo-x": 4, "xxo--oo-x": 4, "x-ooxox--": 8, "-oxoox---": 8, "o-xxxooox": 1, "xx-xo-oo-": 2, "--oox-xo-": 5, "-o---o-xx": 4, "x-xoo-o-x": 5, "-xxo-oxoo": 0, "o-o-xx-o-": 3, "x--oo-xxo": 5, "-o-xxooox": 0, "x-o-o----": 6, "xxooo-xo-": 5, "oxo-x----": 3, "xoxo-o--x": 4, "--x-o-o--": 0, "--o--x-xo": 4, "x---oo---": 3, "x-xoxo-o-": 1, "xo---ox--": 4, "-o--x-o--": 2, "-x-----oo": 6, "-xxo--xoo": 0, "oo-oxxx-o": 2, "-oo-xo-xx": 6, "xox-oox--": 3, "-xoxo-x-o": 0, "-o--o-x--": 7, "-xxx-oo-o": 0, "x-o-o---x": 6, "xxooo-xox": 5, "xxoo-x-o-": 8, "--ox-ooxx": 4, "-o---xoox": 4, "xo-o-xoxo": 2, "oxxxo--o-": 8, "x--o--x-o": 2, "-xo-x-xoo": 5, "x-xoo-o--": 1, "-o---o-x-": 2, "o-xxxooo-": 8, "oxo-x---o": 5, "o-o-xx-ox": 3, "-x--x-oo-": 8, "x-xoxo-oo": 6, "xoxooxx-o": 7, "-o--o-x-x": 7, "x-x-o-o--": 8, "xo---ox-o": 2, "-x-----o-": 8, "xox-o-o--": 7, "--xxo---o": 0, "--x-o-o-x": 1, "o-xx---o-": 4, "-xo---oox": 4, "----xo-xo": 2, "o----oxx-": 8, "--ooox-xx": 6, "o---xooxx": 1, "-oxxooxxo": 0, "-oxoxo-x-": 0, "-ox-xo-ox": 3, "o--oxo-x-": 6, "---oo---x": 5, "o---xxoo-": 3, "oxxx-oo--": 4, "oxooxx-ox": 6, "xo-o-x-ox": 2, "oo--o--xx": 2, "ox--xo--o": 7, "xooox--x-": 8, "o--------": 4, "o-o-x----": 1, "-xx-oxo-o": 0, "ox----xoo": 4, "-xo-xo-ox": 0, "---oxxoxo": 1, "xox--oxo-": 4, "-oxo----x": 5, "oox--oxx-": 4, "x--oxoo--": 7, "-o-oxoxxo": 2, "---oxox-o": 2, "x---ooxo-": 3, "-oxox-oox": 0, "x--ox-xoo": 2, "o-oo--xx-": 8, "oxooxx-o-": 6, "o---xxoox": 3, "o-x-o-xox": 5, "o-------x": 6, "xooxo---x": 6, "ox-xooo-x": 2, "o---xoox-": 1, "o--oxo-xx": 6, "oo--o-x-x": 7, "oox--xox-": 3, "-ox-xo-o-": 8, "xooox--xo": 5, "xoo-xx-o-": 8, "oo--xx---": 2, "o-xxoooxx": 1, "-o-oxoxx-": 0, "oox--oxxo": 4, "o-xxx--oo": 6, "x---ooxox": 3, "---oxox--": 2, "x-xoxooo-": 1, "ox-xx-oo-": 5, "-oxo-----": 8, "---x--o--": 7, "ox--ooxox": 3, "x-oo-x--o": 4, "---o-oxx-": 8, "x--ox-oxo": 1, "oo-xxooxx": 2, "ooxx-----": 7, "--xo-----": 0, "oxoo-xxo-": 8, "-oxo-xx-o": 4, "x---oxo--": 2, "---o-x--o": 6, "o-x-xo--o": 1, "-oo-oxxx-": 8, "x-x-oo-xo": 3, "xoo-o-x--": 7, "xoo-o-xxo": 3, "--x----o-": 4, "-xx-o-oox": 3, "x--xooox-": 2, "o--xx--o-": 2, "-oooxox-x": 0, "-x-oxoxoo": 2, "x-x-o--o-": 1, "-o-o---x-": 0, "x-xo--o--": 7, "x-oxo----": 6, "x-oo-x---": 8, "o-x--oxox": 4, "o-x-xx-oo": 6, "----xooox": 0, "xoo--x-xo": 3, "x-xxo-oo-": 1, "x--o-xoxo": 1, "oo--xxoxo": 3, "oxo-xoxox": 3, "x-x-oo---": 3, "xoo-x-o--": 3, "---xxooxo": 1, "---o-x---": 4, "o-x-xo---": 1, "oxoo-xxox": 4, "xoox-xoxo": 4, "--x--ox-o": 3, "xoo-o-xx-": 8, "-o-o---xx": 5, "xo-ox--o-": 2, "xoo-x--xo": 5, "x-oox-xo-": 8, "o--xx--oo": 6, "oo-xx-o-x": 5, "-x-oxoxo-": 8, "x-x-o--oo": 1, "xoo-o-x-x": 7, "x-xo--o-o": 1, "oo-o--xx-": 2, "-ox-xx-oo": 3, "ox--ox---": 8, "--oox-xox": 0, "-o-ooxx-x": 7, "xo-x-x-oo": 6, "----oo--x": 3, "x-x-oo-ox": 1, "xo-o-o-x-": 4, "-xo-oox-x": 3, "-xxoo--o-": 0, "--x---oox": 3, "oxoxo-x--": 8, "o-oox-x--": 1, "-xooxx-o-": 8, "xo--xxoo-": 3, "--oxooxx-": 8, "-xxo-x-oo": 6, "o--ox-x-o": 7, "-ooxo-x-x": 0, "--x-x-oo-": 8, "-oxoo--xx": 5, "o--oxoxox": 2, "xx-oo----": 2, "x-oo-x-xo": 6, "x-x-oo-o-": 1, "-o---o--x": 6, "o-o-xxox-": 1, "-xx-ox-oo": 0, "xooxxo---": 6, "ox--xxoo-": 3, "----o-xox": 1, "-o-xox-xo": 0, "xo-xx-oo-": 5, "-o-ooxx--": 7, "xo-o---xo": 2, "-xooxx-oo": 6, "-----o-ox": 1, "-x---ooox": 0, "o--ox-x--": 2, "---x--xoo": 5, "-oxo-o--x": 4, "o-oxxo-x-": 1, "o-oox-x-x": 7, "--ooxxxoo": 0, "oox---x--": 8, "-x---o-o-": 6, "ooxo-xxo-": 4, "-xooxxoox": 0, "-o-ooxxx-": 8, "o-x--oxxo": 4, "--xx-oo-o": 7, "o-x---o-x": 5, "ox-o-oxx-": 4, "-o--xxoox": 3, "ox--x--oo": 6, "xo--xx-oo": 3, "xooxoo--x": 6, "--x-oo--x": 3, "xxo-x-o-o": 7, "xoxxoo---": 6, "--x-oo-x-": 3, "x-x-oox-o": 1, "ooxoxo--x": 6, "ooxo---xx": 6, "xx-oo--xo": 2, "xoxoxoo--": 8, "---oxx--o": 1, "-o--xxoo-": 3, "o-xo---ox": 5, "x-------o": 6, "--ox-o-ox": 0, "-o-ooxxxo": 0, "---ox-xoo": 2, "--xx-oo--": 8, "ox-xo-xo-": 8, "ooxxxoox-": 8, "-x---o-ox": 0, "ox--x--o-": 8, "oox--xo--": 3, "x-oxoo---": 6, "--o-o--xx": 6, "-x-x-o-o-": 0, "----oo-xx": 6, "x-oxoo--x": 6, "-o--xoxxo": 2, "--x-oo---": 3, "xoxxoo--o": 6, "x--o--xoo": 2, "xoooxx-o-": 8, "xx-o--o-o": 2, "x---o--xo": 3, "xxo-ox--o": 6, "-ox-x---o": 5, "xo--o-xxo": 3, "xoxoxxo-o": 7, "o-xx-ox-o": 4, "oxox--o-x": 4, "x-ooo-xx-": 8, "x-ox--oox": 4, "-o-oox--x": 7, "-o-xxoox-": 2, "--oxoox-x": 7, "o---xo---": 8, "-----xo--": 8, "----x-oxo": 5, "oo-xx-xoo": 5, "-o-x--x-o": 0, "-ox-oox-x": 7, "-xo--xo--": 4, "xx-o--o--": 4, "x-o-xxo-o": 7, "ooxxoo--x": 7, "--o-xxoxo": 3, "-x--oox--": 3, "--xx-ooxo": 1, "oox---ox-": 3, "-oxox-oxo": 0, "x-o--ox--": 8, "-xoo-xox-": 4, "x---oox--": 3, "oxo-xx-o-": 3, "-x-x---oo": 6, "ooxxoo-xx": 6, "-ox------": 8, "--oxoox--": 0, "xo-xxoo--": 8, "oxxx-ooxo": 4, "ox--ooxx-": 8, "----o--x-": 0, "xo--oxoxo": 2, "oxo-o--xx": 6, "ox--o-xo-": 8, "-xoooxxo-": 0, "-oxxxooo-": 8, "---oxoox-": 1, "ox-o--xox": 2, "-oo-x-xo-": 0, "o-xoxo-xo": 6, "o--oxox-x": 7, "--oo-x---": 0, "o-xo-xx-o": 4, "xox--ooxo": 3, "xoo-xoox-": 8, "-ooxoo-xx": 6, "-xoxx-o-o": 7, "-ooxx-xoo": 0, "xoxxoo-xo": 6, "o-ox-x-ox": 4, "x---oo-x-": 3, "oox-xx--o": 6, "--oo-x--x": 0, "ox-o--xo-": 8, "xoooxox--": 8, "oox---o-x": 5, "-oo-x-xox": 0, "xo--x-xoo": 3, "--xoxooox": 0, "o-xoxo-x-": 1, "-xoooxxox": 0, "ox--o-xox": 2, "-o-xx---o": 5, "--xxoox-o": 0, "x--x-oo--": 2, "ox-xox-o-": 8, "o-xoo-xox": 5, "xooo-xx--": 8, "-oo--o-xx": 0, "o-ox-ox-x": 7, "oo-ooxxx-": 8, "-o--xox--": 2, "xxo-ooxox": 3, "ox-oxo---": 6, "-o---oxox": 4, "xo-oo-x-x": 7, "oox-xx-oo": 3, "-oxoxx-oo": 6, "x-ox-ooox": 4, "-oo-xxo-x": 3, "oxoxx-o--": 8, "x--ooxo-x": 2, "---xoo---": 8, "--o-xoxox": 0, "xo-ooxxxo": 2, "ox-o-ox-x": 7, "o-o-xxoxo": 3, "o-x--o---": 3, "-xooxxo-o": 7, "-x-o-o-ox": 4, "x-o-o-x-o": 3, "o--xx-oxo": 2, "o-o-xooxx": 1, "o---xo--x": 6, "ooxxx-oo-": 5, "x-o----xo": 5, "oxo-xxoo-": 3, "xx-oo-xoo": 2, "xx-o-x-oo": 2, "x--o----o": 2, "x--ooxo--": 2, "---xoo--x": 6, "oox-xo--x": 6, "o--o-ox-x": 4, "o--x-xoox": 4, "oxo--o-xx": 3, "-oxoxx-o-": 0, "-x-ooxx-o": 0, "oxoxx-o-o": 5, "xoo--oxx-": 3, "ooxxx-oox": 5, "-xox--xoo": 5, "x---o-ox-": 2, "o-x---xo-": 5, "ox-o-o-xx": 4, "o--xooxx-": 8, "oxo-xxoox": 3, "--o-xoxo-": 8, "xx-oo-xo-": 2, "oxx-oxo--": 8, "o-x--o--x": 6, "o---xoxxo": 1, "oxx-o-oox": 5, "oxoox-x-o": 7, "-o-xoo--x": 7, "-xx-ooox-": 0, "x-oo----x": 7, "--ox-oo-x": 4, "xx---oo--": 2, "-xxxo-o-o": 0, "o-o---x-x": 7, "-xooxox--": 7, "oox-ooxx-": 8, "-x-o-xoxo": 4, "xo----ox-": 4, "---xo-o-x": 2, "o--xxo--o": 2, "-o-ox--ox": 0, "-o-oxxox-": 0, "o-x-xoox-": 1, "x-ox----o": 6, "x-o-x-xoo": 3, "xx-o-oo--": 4, "------o-x": 0, "xo---o-xo": 2, "xooo--xox": 4, "x---ox-o-": 1, "x----xo-o": 7, "xooox-x-o": 5, "xo-xoo---": 6, "o--o--xx-": 4, "oxo-xoo-x": 7, "oxoooxx--": 8, "oox---oxx": 5, "-x-xoo---": 0, "xoxo-ox-o": 4, "ooxx-x--o": 4, "--xo--x-o": 1, "-o-o--xx-": 4, "-o--xxoxo": 3, "ooxxx--o-": 6, "o-x-ox---": 8, "-xx-oooxo": 0, "o---xx-o-": 3, "xxox-ooox": 4, "----oxo-x": 2, "-xoxx--oo": 5, "xx--ooox-": 2, "xo----oxo": 2, "-o-o-xxxo": 0, "--oxxo-ox": 0, "xxo--oxo-": 8, "o--xxo---": 2, "ooxox--ox": 6, "x-oo-----": 4, "o-xx-xoo-": 4, "x-ox-xo-o": 4, "oxoooxx-x": 7, "o-xxxo-o-": 6, "o--ox--ox": 6, "oxooxx---": 7, "ox-xxoxoo": 2, "xo-xoo--x": 6, "x-xooxo--": 8, "-ooxx-x-o": 0, "xo---o-x-": 6, "o-o-x-ox-": 1, "o--o--xxo": 4, "-o-oxxo-x": 2, "------o--": 4, "ooxxxoo--": 8, "ooxoxx-o-": 6, "xo--xo--o": 2, "oxx--oox-": 4, "---ox-xo-": 8, "--oo--xox": 1, "xxoox-oo-": 8, "x---xoo--": 1, "xx----o-o": 7, "-ox-o-x--": 7, "x-oox----": 8, "xooo--oxx": 4, "xox--oo--": 4, "-ox--oxox": 4, "xx-oox--o": 2, "o---x----": 7, "----ox-xo": 0, "oxo---xox": 4, "-ooxx-xo-": 5, "x-ooxx--o": 1, "xx-x-o-oo": 6, "-oxox-ox-": 0, "xoxoo--x-": 5, "-xo----o-": 6, "-oox-ox-x": 7, "x--o--ox-": 1, "ooxx-ox-o": 4, "o-x---x-o": 4, "-xooo-xx-": 8, "ox-oxx-o-": 6, "oxooxxx-o": 7, "oxoxoox-x": 7, "xox--oo-x": 4, "o-x-xxoo-": 3, "x-oox---o": 5, "ox-xx--oo": 5, "-x-oxo--o": 2, "o--xxo-xo": 1, "-xo--o-ox": 3, "xo--o-ox-": 2, "-xoox-x-o": 7, "-xo----ox": 3, "oxo---xo-": 4, "-x-xooxoo": 0, "-xo-xooox": 0, "xx--ooxo-": 3, "x--xo-o--": 2, "xo----x-o": 4, "----xox-o": 2, "-o-x-oxox": 4, "xoox-o---": 8, "x---x-oo-": 8, "x-oo-xox-": 4, "oxo-o-xox": 3, "xox-xooo-": 8, "xo-oxoox-": 8, "-o-xxo-o-": 0, "oo-oxx--x": 2, "---x-oxo-": 2, "-x----xoo": 2, "oxxx-ooox": 4, "-ox-oooxx": 3, "--xoo----": 5, "oxoxo-xo-": 8, "o-x--xxoo": 4, "-oxox--ox": 5, "-oo--ox-x": 7, "--xooxo--": 0, "x-xxoo-o-": 6, "---oo--xx": 5, "-xoo-o-xx": 4, "oox-xooxx": 3, "-x--xoxoo": 2, "---o-----": 5, "-o-xxo-ox": 0, "xooox----": 8, "ooxxox---": 8, "--x-xooo-": 8, "xo---xxoo": 4, "-xxxoo--o": 0, "xoox-o--x": 4, "-x--o-o-x": 2, "-oxx--o--": 5, "o--x--o-x": 5, "oox-xoox-": 3, "xxooxxoo-": 8, "o-x----xo": 4, "---o----x": 6, "--xoo---x": 5, "x-xxoo-oo": 6, "--xo-o-ox": 4, "--oxx---o": 5, "x-xoxoo-o": 1, "-ooxxooxx": 0, "oxo-ox-ox": 6, "oxoxo-xox": 5, "x-xxo--oo": 6, "-oxox--o-": 8, "----xo--o": 2, "xoo-ox-x-": 6, "-ooxx--ox": 0, "o--o-x---": 6, "x-xox-oo-": 1, "o--ooxx-x": 2, "-oxxo--xo": 0, "ox-x-ooox": 2, "--xox-oox": 5, "o-o---xx-": 1, "oxxoox---": 8, "-x-o-xo--": 0, "o---x-x-o": 3, "-oxxo-oxo": 0, "xo--ox---": 7, "xo--ox-xo": 3, "o-x-xo-xo": 6, "---oox--x": 6, "x-x-ooxoo": 3, "xoxo--xoo": 4, "oxo-o-x-x": 7, "o-x-xooxo": 1, "xox----o-": 4, "ox-xooxo-": 8, "x-xxoooox": 1, "x-o--o--x": 4, "o-xxoo-x-": 8, "---oox-x-": 8, "xo--o----": 7, "oox---xox": 5, "x-o-oox--": 3, "o--ooxx--": 8, "xoo-ox-xo": 6, "xoxo-oxxo": 4, "----xo---": 2, "-oxx-ox-o": 4, "xo-x----o": 4, "xxooox---": 6, "-x-ox-xoo": 2, "-oo--xx--": 0, "-ooxx--o-": 5, "o--o-x--x": 2, "xxoooxxo-": 8, "-o--o---x": 7, "oxoo--x-x": 7, "-oxxo-ox-": 8, "-oo-o--xx": 6, "-o--xxxoo": 2, "x-xxoooo-": 1, "xo--o---x": 7, "x-xo-ooox": 4, "xoxo--xo-": 4, "---oox---": 6, "----o----": 6, "o--xoxo-x": 2, "-ooo-xxx-": 8, "oox-o-oxx": 5, "xo-----o-": 4, "-xxoxo--o": 0, "--o-x-xoo": 5, "x--xoo-xo": 2, "x-xoo--ox": 5, "--ooxx--o": 1, "xx-oxoo-o": 7, "x-xox--oo": 6, "x---o-xo-": 1, "oxox-o--x": 7, "--xoxo--o": 7, "o-ooxo-xx": 1, "--ooxooxx": 1, "xo-xo-oxo": 2, "---ox-o-x": 0, "--o--x---": 4, "oox-x-o--": 3, "x--xo---o": 2, "xooo---x-": 8, "o-x---oox": 5, "xo-oxx-o-": 6, "---ox-ox-": 1, "--o-oxxxo": 0, "-oxx-o-o-": 4, "x----oxoo": 3, "-xoxo----": 6, "o--x-oo-x": 1, "xxoxo---o": 6, "--o-x-xo-": 0, "o-o-xoxox": 1, "xxoo-xoxo": 4, "oo-xoox-x": 7, "-o-ooxoxx": 2, "xo-----xo": 3, "o----o-xx": 4, "--ooxx---": 6, "x-xoo--o-": 1, "x---o-xoo": 1, "--xoxo---": 0, "xooo---xx": 6, "o-xxooox-": 8, "-o--ooxx-": 8, "o--o-xxox": 2, "o----xo-x": 2, "--oxoxx-o": 0, "o-o--ox-x": 7, "---ox-oxo": 1, "o-x-oxxo-": 8, "oox-x-o-x": 5, "-oo-xx--o": 3, "x--ox--oo": 6, "x-xo--oxo": 1, "ox-oo-xox": 5, "ox-ox-xo-": 2, "x--o---xo": 1, "ooxx---xo": 4, "---xoxoox": 2, "-xo-xx-oo": 3, "xo-xx--oo": 6, "--xxxo-oo": 6, "-ox-oo-x-": 3, "o------x-": 6, "xooxo--x-": 6, "--oxx-oxo": 1, "xooo-xxxo": 4, "ox-xoo-ox": 6, "x-oxxo-o-": 8, "-ooxxo-ox": 0, "x-oooxxox": 1, "-ox-ox---": 8, "xxoo--ox-": 4, "x--ox--o-": 2, "-oo-xx---": 3, "oo-xx-ox-": 5, "---x----o": 6, "ooxx--x-o": 4, "ox-ox-xoo": 2, "xox-oxoxo": 3, "o-xoxx--o": 6, "-xox-oox-": 4, "o--xxoo-x": 2, "--x--ooox": 0, "o--o--xox": 2, "-----oo-x": 3, "ox-x-o-ox": 2, "ox-o-xxoo": 4, "xooxo--xo": 6, "-xo--ox--": 8, "xo--oxx-o": 3, "x-o-x---o": 5, "oxo-xx-oo": 3, "oo--xx-xo": 3, "-ox-oo-xx": 6, "-oxxooo-x": 7, "---oxoxxo": 2, "-oo-xo--x": 0, "--xxoooxo": 0, "o-x-o---x": 7, "oo-oox-xx": 2, "--x--o-ox": 4, "-ox--oxxo": 4, "x---oo--x": 3, "oox--xxo-": 4, "---ooxxxo": 0, "o--xoox--": 8, "oxx---xoo": 4, "xoo--ox--": 3, "-o-o-xx-o": 4, "-xxox-oo-": 0, "x-x-o-oxo": 1, "oox-x--xo": 3, "oox--xx-o": 4, "-o--o-oxx": 2, "x--xxooo-": 8, "-x--oo--x": 3, "-oo-xx-xo": 3, "-o----xo-": 4, "xox-o-x-o": 3, "xoo--ox-x": 3, "o--xoox-x": 7, "xx-o--oxo": 4, "--xxxoo-o": 7, "oxxxooox-": 8, "--x--o-o-": 0, "xoo-x--o-": 5, "o-x-o----": 8, "--o----ox": 1, "xoox---ox": 6, "x-o---ox-": 4, "-x-oox---": 2, "xx--o--oo": 6, "ox-xo-o-x": 2, "--oxxoox-": 1, "xo--oxo-x": 2, "x-x-o-o-o": 1, "o-xx-ooox": 4, "o-o-xo-xx": 1, "o---xox--": 8, "--ooxxo-x": 0, "--x-ox--o": 0, "----oox--": 3, "ox---x-o-": 4, "o----oxox": 4, "x-oox-o--": 7, "--xoo-oxx": 5, "xox--o---": 6, "o--xo---x": 2, "oo-xx---o": 5, "--oxxoxo-": 0, "x-oo-o-xx": 6, "--o-xoo-x": 1, "-ox-ox-xo": 0, "oo-xx-x-o": 2, "-xooxo--x": 0, "xoooxo-x-": 8, "-oxxoo-xo": 0, "x--ox-oo-": 8, "--oo-o-xx": 4, "---x--oxo": 4, "x-oo-oxox": 4, "x-ox-o-ox": 4, "o-xxoo-ox": 1, "xoox--ox-": 4, "--ooxxo--": 0, "o-o-xo-x-": 1, "ooxxxoo-x": 7, "x-oooxxxo": 1, "-xxox--oo": 6, "oo-xx----": 5, "-xooxo---": 7, "x-x-xoo-o": 1, "oxoxx-oo-": 5, "o-xxxooxo": 1, "ox-x-oox-": 4, "-oxxoo-x-": 6, "--oxo--x-": 6, "oxxxxo-oo": 6, "o-xxox-o-": 8, "oox---xxo": 4, "xxoxoo-o-": 6, "xo-oxxoo-": 8, "-o-oo-x-x": 7, "oxoxxoo-x": 7, "o-x--xo--": 3, "---xo-xo-": 0, "o--oxxxoo": 2, "xo-oo-xxo": 5, "xx--o--o-": 6, "--o--ox-x": 0, "oxx-xo--o": 3, "--xxo-o--": 0, "-xxooxo--": 0, "--xxo--o-": 1, "oo--xxoox": 3, "xo-xoo-xo": 6, "-xxxoooxo": 0, "oxoxxoo--": 7, "-xo-x---o": 5, "x-ooxoox-": 8, "oxoxx-xoo": 5, "xxoox--o-": 8, "o-xox--ox": 6, "---xo-xoo": 0, "xxoxoo-ox": 6, "o-o-x-xo-": 1, "x-oo-xxoo": 1, "xo-oo-xx-": 8, "xxoo-xoox": 4, "xo-o-xoox": 2, "o-o-x--x-": 1, "ox--x-o--": 7, "oxoo-oxx-": 4, "-xxooxoo-": 8, "---o-o-xx": 6, "xo-xoo-x-": 6, "o-oxxo-ox": 1, "xox-xo-oo": 6, "--ox--ox-": 4, "xo-oox-x-": 8, "---oxoo-x": 0, "oxoxoo--x": 6, "-xxo-o-xo": 4, "xoxxooox-": 8, "ox-------": 6, "-ox--oo-x": 4, "xoxoo-ox-": 5, "o---o-xx-": 8, "oxx-x--oo": 6, "-oo-xoxox": 0, "-x-o--xo-": 2, "-x-ox-o-o": 7, "ooxxoo-x-": 8, "x-xoo-x-o": 1, "o--xxox-o": 2, "--xoox---": 8, "--ox-o-x-": 8, "x-o-xoox-": 8, "xx-ooxoox": 2, "xoxox---o": 6, "----x-o--": 2, "xoooxx-xo": 6, "oxxo-oxox": 4, "-xox-o-ox": 0, "xxo-xo-o-": 8, "o-xxo--ox": 5, "xxo-ooxo-": 3, "oxxo-xxoo": 4, "-oooxx--x": 0, "xx-o---o-": 2, "oxoxox-ox": 6, "oo-ox--xx": 6, "-oo-oxx-x": 7, "x--o--o--": 1, "-x-o--xoo": 2, "xo---xoox": 2, "-o-xx--o-": 0, "-x-ox-o--": 0, "x-ooox-xo": 6, "--xoox--o": 0, "ox--xox-o": 7, "-oxoxo---": 6, "xo-o-x-xo": 6, "o--xo-xox": 1, "x--o--o-x": 5, "-oo-ox-xx": 6, "xoo---xo-": 3, "-oo-xxxo-": 3, "ox-xo--ox": 2, "xxoo-oxox": 4, "-x-oo--ox": 5, "xx-xoo-o-": 6, "-oox-o-xx": 6, "-x--ox-o-": 2, "o-oxx-x-o": 5, "xoxo-----": 4, "-xx-oxoo-": 0, "x--xooo--": 2, "--ox-ox--": 0, "xox--oox-": 4, "o---x--o-": 3, "-xxxoo-o-": 0, "-oxxxooox": 0, "-xoox----": 8, "o--x--xoo": 4, "---x-oo--": 2, "oxoxx--o-": 5, "ox-o-x-xo": 4, "oox-xxo-o": 3, "ooxo-xxxo": 4, "-xxoox-o-": 8, "ox-oxoxox": 2, "-o---oxx-": 8, "oo-xxo-ox": 2, "-o-o-xxo-": 4, "x--xooo-x": 2, "-ooxo--xx": 6, "-ox-o--xo": 0, "xooo-xxo-": 4, "o-oxx-o--": 5, "xo-x-o-ox": 4, "xoxo----o": 7, "ooxxo---x": 5, "xo-o-ox-x": 4, "-xxxoo-oo": 0, "---xoooxx": 2, "-xoox---o": 7, "--oxxo-o-": 8, "o--x--xo-": 4, "-oo-xxxoo": 3, "ox-oxoxo-": 2, "oxo-x-x-o": 5, "x-o-ooxx-": 8, "-xxoox-oo": 0, "---x-oo-x": 1, "-oxoxo--x": 7, "oox-----x": 4, "o-xx-oox-": 4, "-x--xoo-o": 7, "xo--xo-xo": 2, "-oo-x---x": 0, "o-oxoo-xx": 6, "oxoo--xox": 4, "-oxo-o-x-": 4, "-xx---oo-": 8, "-xoxooxo-": 0, "x-o--xoox": 4, "xx--xoo-o": 7, "o---x-oox": 3, "xoox-o-x-": 6, "--xox--o-": 8, "xo-o-xo-x": 7, "oo-o-x-xx": 6, "-xx-o---o": 0, "o-xx-xo-o": 4, "-o--ox--x": 7, "xo-oxoxo-": 8, "xox-xo-o-": 3, "x---o-o--": 2, "-----oxox": 4, "-oxx-ooox": 4, "xoo-xxo-o": 3, "-x--o-xo-": 0, "--x-xo-o-": 8, "ox-ox--ox": 6, "---xx-oo-": 5, "oxxoxo--o": 6, "-ox-xxo-o": 3, "-xoxooxox": 0, "-x--xoo--": 8, "xoooxxox-": 8, "o-ox-xx-o": 4, "o-xx--oxo": 4, "ooxx-o---": 8, "x-oo--x--": 8, "oox------": 8, "-ooxx-oox": 0, "-oxo-o-xx": 6, "-oo-x----": 0, "-o--xx-o-": 0, "-o-oo-xx-": 8, "----o--ox": 1, "ox-ooxx--": 8, "o-o-x--xo": 1, "o--xoooxx": 2, "---o-xx-o": 4, "xo-ooxx-o": 7, "x--o-oxo-": 4, "xo-o-xo--": 8, "-x--o-xoo": 0, "-xoooxxxo": 0, "xx-o-o-xo": 2, "oo--xx--o": 2, "oxxoxo---": 6, "--x-xo-oo": 6, "xxo-o-xo-": 3, "-xoxoox--": 0, "x--oxxo-o": 7, "x----oox-": 1, "-o-oxxxoo": 2, "o--xx-oo-": 5, "-xo-oxxoo": 0, "-oxxoxo--": 8, "x-oox--xo": 1, "-o-oxox-x": 7, "o--oxx--o": 6, "x-ooxxoxo": 1, "xx--ooxoo": 2, "xx--oo---": 3, "xo-xox--o": 6, "-oxxxooxo": 0, "-----o-x-": 4, "x-x-oxoo-": 8, "o-o-xxo--": 3, "-xxxoooo-": 0, "oox--ox-x": 3, "--oox---x": 1, "--xxoo-ox": 1, "-o-xx-o--": 5, "xxo-o-xoo": 3, "-o-o-xxox": 4, "-o-oxox--": 0, "o--xx-oox": 5, "-xxoo-o-x": 0, "oxxxo-o--": 8, "x----oo-x": 4, "x-xo-o--o": 4, "--xoo-x--": 5, "o-xxxoo-o": 7, "-xxxoooox": 0, "o-o-xxo-x": 3, "o--oxx---": 6, "-o--x--ox": 3, "-oxxoxoxo": 0, "xo-ox-xoo": 2, "--xxoo-o-": 1, "--oox----": 6, "-o--xo-ox": 0, "--xxooxoo": 0, "oo-oxox-x": 7, "x-xx-o-oo": 1, "o-o-xo--x": 1, "-x-x-ooxo": 4, "-------o-": 8, "ox---xoox": 3, "-o-xx-o-o": 5, "xxoo---ox": 4, "xo-o---x-": 8, "-oxx-xo-o": 4, "--xx-o-oo": 6, "o--x-ox--": 8, "--ox-xoox": 4, "-ox----ox": 4, "oxo-x--ox": 5, "-xoo-oxox": 4, "ox-xxooo-": 8, "oo--oxx-x": 7, "x--o-xoox": 4, "x--x-ooox": 2, "xooooxxx-": 8, "-oxxxo-oo": 6, "x-x-ox-oo": 1, "-o-o--x--": 8, "x--oox--o": 6, "ooxx-xoo-": 8, "x-x--o-oo": 1, "xooxx--oo": 5, "--o-x-o--": 3, "-xo---o-x": 4, "xx-xo-o-o": 2, "-oo-o-x-x": 7, "-o-oxx--o": 6, "xooxx-o--": 8, "-xox--oox": 4, "---xooxox": 0, "x--o-xoo-": 8, "--x-oxo--": 0, "xo--x--oo": 6, "ooxooxxx-": 8, "---o--x--": 7, "ooxxxo---": 6, "-xx-xo-oo": 6, "-----xoxo": 4, "ooxxx-oxo": 5, "ox-xxooox": 2, "o--o-oxx-": 4, "-x-ooxxo-": 2, "--o-xo--x": 7, "-ox----o-": 4, "xo--xoo--": 8, "oxxox---o": 7, "xxooxx-oo": 6, "--o-x-o-x": 3, "--xo-x--o": 6, "xx-oo--ox": 2, "---xooxo-": 0, "-oxxx-o-o": 5, "---x---o-": 6, "x-x--o-o-": 6, "xooxx--o-": 5, "x--oox---": 2, "----x-o-o": 7, "o-xxx-o-o": 5, "---xxoo--": 1, "oxx--oxoo": 4, "-o-oxx---": 8, "xooxx-o-o": 5, "-o-o--x-x": 0, "xoox----o": 5, "-o------x": 4, "xxoo-x--o": 6, "-xo-xoxo-": 8, "xox---xoo": 4, "-o-xxooxo": 2, "ooxoxx-xo": 6, "--oooxxxo": 0, "o--ox--x-": 6, "-xo---xoo": 5, "o-x--x-o-": 6, "ooxoo-xx-": 8, "---x-o-xo": 2, "-xx-oo---": 0, "--oxxo---": 8, "ox-oxo--x": 6, "x-x-ooo--": 1, "oo-oxxxo-": 2, "o-oox--xx": 6, "xo--o-x--": 7, "oo--xo-xx": 6, "x-o--x--o": 3, "ox--oox-x": 7, "x-xoo-oox": 1, "--x-o--xo": 0, "--x-oxoxo": 0, "--o-o-x-x": 3, "--o--xx-o": 3, "------x-o": 0, "oxo--oxox": 3, "o-x-x---o": 3, "oo-x-o--x": 2, "-ooxo-xx-": 0, "o--ox--xo": 6, "o--oo-xx-": 8, "-o-------": 2, "xoox-x--o": 7, "oox-o-x-x": 5, "-xx-oo--o": 0, "oo--xo-x-": 2, "o-oox--x-": 1, "-x--x-o-o": 7, "-xxo--oxo": 0, "o-xx----o": 4, "xxoo--oxo": 4, "ooxoo-x-x": 5, "-x-xoo-ox": 0, "ox-xooxox": 2, "xo--o-x-o": 3, "oxo--x-ox": 4, "oo-oxxxox": 2, "x-x--ooox": 4, "oxoo-xx-o": 4, "x-xo-xoo-": 8, "----xxoo-": 8, "ooxxxo--o": 6, "o-x-o--ox": 5, "ox-xoo--x": 7, "ox--xo-o-": 6, "x-ooo-x-x": 7, "o-oxx-o-x": 5, "oxxoo---x": 5, "x-xoox--o": 1, "--o-ox--x": 6, "xxoo---xo": 4, "-o----xox": 4, "x-oo-xx-o": 4, "o-o-xx-xo": 1, "ox-x--o--": 4, "-o-ox--x-": 8, "xxo-oox--": 3, "o-xoxo---": 6, "o--xxoxoo": 2, "xooo-xxox": 4, "x--o-x-o-": 2, "xooxx-oxo": 5, "oxo-xo-ox": 3, "xoo-xo-x-": 8, "---oxooxx": 0, "oxoo-xx--": 7, "ox--xo-ox": 3, "o-x--ox--": 7, "-oo-xxo--": 0, "x-x-o-xoo": 3, "oo-xxox--": 2, "xo-xoxoxo": 2, "oxo---oxx": 4, "-ox-xo--o": 6, "xox--o-xo": 6, "o--oxox--": 1, "oxx-oo-ox": 3, "o-xoxo--x": 6, "o------ox": 4, "oxox--xo-": 8, "-o-ox--xo": 2, "xoxxo---o": 6, "o-o-x-xxo": 1, "-xx-oooox": 0, "x--o-x-oo": 6, "xx--oooox": 2, "x-x----oo": 6, "xxooox-xo": 6, "o-oxxoo-x": 1, "o-oxx---o": 5, "-oxoo-x-x": 7, "-ooox-xx-": 8, "xo-oxxoxo": 2, "o-oo-xx-x": 7, "-oooxxxo-": 0, "xoxo--o--": 8, "-oxxxo-o-": 0, "ox-xoo-x-": 8, "---oxo-xo": 2, "xoxxxooo-": 8, "-----o--x": 7, "oo-xooxx-": 8, "-x----oox": 2, "oo-xx--xo": 2, "xo--xxo-o": 3, "--o-xxo-o": 7, "--oo--xx-": 8, "o-oox-xox": 1, "-xo-xxo-o": 7, "o-ooxxxxo": 1, "o-oxx----": 1, "xoxo--o-x": 5, "-oooxxxox": 0, "o-o-ox-xx": 6, "-o-oxxoox": 2, "--x-o-oox": 5, "xox-ooxxo": 3, "o-xx-o-xo": 4, "x--o--xo-": 4, "ox---ooxx": 4, "o-oo-xx--": 1, "--ooxxoxo": 1, "--xxoo-xo": 0, "-------ox": 5, "o-ooxoxx-": 1, "-x-x-oxoo": 2, "xo--x--o-": 2, "oxxx-oxoo": 4, "x--o-oxox": 4, "--oox-oxx": 0, "xoxoxo-o-": 8, "-x----oo-": 8, "--ooxox--": 8, "ox--oxxo-": 8, "-----ooxx": 4, "x-oo-x-ox": 4, "-ooxxoo-x": 0, "xo-o-xxoo": 4, "-----x-o-": 4, "xx-xoo-oo": 6, "xo---oox-": 2, "x-o-o-x--": 3, "xooxxo-o-": 6, "oo--xx-ox": 3, "-xoo-x-ox": 6, "ooxx-oo-x": 4, "ox----x-o": 4, "-o-xxoo--": 2, "xoo-xx--o": 3, "xoxo-ooxx": 4, "xooo-xo-x": 4, "-xo-ox-ox": 6, "xo--xo-o-": 8, "oo--x-xo-": 2, "-ox-x-oox": 5, "o--ooxxx-": 8, "--ox-o--x": 7, "ooxxo-oxx": 5, "---ox--o-": 8, "oo-ox-x-x": 7, "-x--oxoox": 2, "oxo-ox--x": 6, "-xxx-ooo-": 0, "--x-oox--": 3, "x---oox-o": 3, "-xxo-ox-o": 0, "o-oxx--xo": 1, "xoxoo---x": 5, "-o-xxoo-x": 0, "xoxo-oox-": 4, "o-x-o-x--": 8, "oo--xx-o-": 3, "-ox---x-o": 0, "xo---ooxx": 4, "x-ooxxxoo": 1, "---xooxxo": 0, "---ooxo-x": 2, "--o-o-x--": 0, "-x------o": 2, "oo-ox-x--": 2, "-o-xoo-xx": 6, "xoxxooo--": 7, "--o-xo---": 8, "o----x---": 2, "-ox-x-oo-": 8, "oo--x-xox": 2, "---ox--ox": 0, "ooxxo-ox-": 8, "x-x-oo--o": 3, "xooox-ox-": 8, "o-o-x-x--": 1, "o-x-xoo--": 3, "--ox-o---": 8, "ooxx-oox-": 4, "-xxx-o-oo": 0, "xoo-----x": 3, "xo-x---o-": 6, "o-xxo-ox-": 8, "ooxxx--oo": 5, "ooxx--o-x": 5, "---x-oxoo": 0, "o---xx-oo": 3, "xo-ox---o": 6, "o--xx---o": 1, "xo-ox-x-o": 2, "xooox-xo-": 8, "--o---oxx": 4, "xox-oxo--": 8, "x-o-xxoo-": 3, "x-xoxoo--": 7, "ooxx---ox": 4, "-o-xoxx-o": 0, "o---xo-ox": 6, "o--oxoxxo": 2, "--x-o--o-": 1, "--x-xooox": 0, "xo-oox-xo": 6, "-xoo-xx-o": 7, "-----xoox": 0, "oxox---ox": 5, "--xo-xxoo": 1, "---xoxxoo": 0, "xx-xooo--": 2, "xoo--xxo-": 4, "xoo------": 3, "-ox--x-o-": 4, "o--oxx-xo": 1, "ooxx-ooxx": 4, "xo-ox----": 6, "---oxxo--": 0, "oo-xo-x-x": 7, "--x-o--ox": 5, "-oxo---ox": 5, "-xoo--xxo": 4, "xx-ox--oo": 2, "ox--x---o": 2, "-x-xo-o--": 2, "x-xooxxoo": 1, "-oo---xx-": 0, "o--oxoxx-": 8, "oxooxx--o": 7, "xooooxx--": 7, "-ox----xo": 4, "x-oo-x-o-": 6, "-xxo---o-": 0, "-ox-x--o-": 8, "xxo---o--": 4, "---o-x-o-": 6, "oo--xox-x": 2, "x-o--ooxx": 4, "-o-o-x--x": 0, "o--oxxxo-": 2, "-o--x--o-": 6, "--xx-o-o-": 0, "xx-ooxoo-": 2, "xx-o-oox-": 4, "x-oooxx--": 8, "-o-o-ox-x": 7, "x-oo--oxx": 4, "-xo-o-x--": 0, "xoo---xox": 3, "-x-xooxo-": 0, "oxx----o-": 8, "-x-xo---o": 0, "-o----xxo": 0, "-xo--x-o-": 8, "--xx-ooox": 0, "xx-o--oo-": 8, "oox--x---": 4, "oox--x-xo": 4, "x---oxoxo": 2, "x-xxo-o-o": 1, "-o-o-x---": 6, "x-oxx--oo": 5, "--xxo-oox": 5, "x--o-xo-o": 7, "--o------": 4, "-ox-x--oo": 6, "oxoxxo---": 7, "ox---oxo-": 8, "o-xxxo-oo": 6, "xox---o--": 8, "-o-oxxo--": 0, "---o-x-ox": 4, "-xoxx-oo-": 8, "x-o-xx-oo": 3, "----xo-o-": 6, "-xx--oxoo": 3, "----ooxx-": 8, "x-oooxx-o": 7, "-x-oxox-o": 2, "xo--o-oxx": 2, "ooxo-oxx-": 8, "xx-o--oox": 5, "--x--oox-": 1, "xx-ox-oo-": 2, "-o-o-xx--": 2, "oxoxxoxo-": 8, "x-o--xxoo": 3, "oox--x--o": 4, "-xxox-o-o": 0, "o-oo--x-x": 7, "o-xxooxox": 1, "-xo-o--ox": 6, "--oxxooox": 0, "-x-o-oxo-": 4, "-o-xx-oxo": 5, "--oox-x--": 8, "x-oxoo-x-": 6, "x-o---x-o": 3, "-x-ooxxoo": 0, "--o-oox-x": 3, "x-xo----o": 1, "xox--ooox": 4, "-ooox-x-x": 7, "o-ox-xxo-": 4, "o-xx--oox": 5, "x---x--oo": 6, "xooxoo-xx": 6, "xooo-x--x": 6, "--x---o--": 8, "-o-oxo--x": 2, "-o-xo-oxx": 2, "o-x--o-ox": 4, "-ooxooxx-": 8, "o-oxx-xoo": 5, "-ooox-x--": 0, "ox-oox--x": 2, "oox-xxo--": 8, "oo--oxxx-": 8, "x-xo-o-ox": 4, "--oox-x-o": 5, "--o-xxo--": 3, "-ox-o--x-": 8, "o-x-x-oox": 5, "xo--xo---": 3, "x-x--ooo-": 1, "xo---oxxo": 3, "oox-x--o-": 6, "o-o-x-oxx": 1, "oo--x----": 2, "o-o-xox-x": 7, "---oo-x-x": 7, "xoooo-x-x": 7, "-----ox--": 4, "-oooxx-xo": 0, "-xoo--x--": 7, "x-o------": 6, "o---oxoxx": 2, "xoo-xxxoo": 3, "-ox-xoo-x": 0, "xooo-x---": 7, "xooxoo-x-": 6, "--oxo---x": 6, "o-oxx-xo-": 5, "xooo-x-x-": 8, "xxo---oox": 4, "o-o-xxxo-": 3, "ooxoxo-xx": 6, "xo-oox---": 7, "oxoox-x--": 7, "--x-oooxx": 3, "o-oxxoox-": 1, "-ox-xoo--": 0, "ooxx-o--x": 6, "xoxoo-oxx": 5, "oox-xoo-x": 3, "--xx-ooo-": 8, "xoxo---xo": 4, "oxoxx---o": 7, "xxo--o-ox": 6, "-oxoo--x-": 5, "ox-o-xxo-": 2, "-ooxx--xo": 5, "xoxo-xoxo": 4, "o---o-x--": 8, "-oxoox-xo": 0, "--o-xox--": 8, "-o--xx-oo": 6, "o---oox-x": 7, "--xxoooox": 1, "xo--ooxx-": 8, "xo--ooxxo": 3, "xxoo-xxoo": 4, "-xoxxooox": 0, "-oxx--xoo": 0, "-xooxxo--": 7, "o-oxxooxx": 1, "o-o-xxxoo": 3, "-oxoxx--o": 6, "xooo-o-xx": 6, "ooxox----": 6, "-oox-xx-o": 4, "xo-oox--x": 2, "x--oxo-o-": 2, "x-oxo--xo": 6, "oxo-x-oox": 3, "-xo-oo-xx": 6, "ox-o----x": 6, "xooooxx-x": 7, "xoo-x-x-o": 3, "--ooxoxox": 0, "o---o-x-x": 2, "xx-oo-x-o": 2, "xoxxooo-x": 7, "oo-x-x-ox": 2, "o--x--ox-": 4, "-xxoo-x-o": 0, "-xoo-oxx-": 4, "--ooxxx-o": 7, "xo---x--o": 3}

class EnforcedTimeExecption(Exception):
    pass

def EnforcedTimeHandler(signum, frame):
    raise EnforcedTimeExecption()

class Player61(object):
    def __init__(self):
        self.number_of_moves = 0
        self.player_symbol = None
        self.opponent_symbol = None
        self.actual_board = [[]] 
        self.status_board = []
        self.backup_status_board = []
        self.transposition_table = {}
        self.heuristic_minimax_table = heuristic_table
        self.is_max_player = True

    def make_board_str(self):
        string = ""
        for i in xrange(0,9):
            for j in xrange(0,9):
                string += self.actual_board[i][j]
        return string

    def make_block_str(self,board,block_number):
        x,y = self.get_block_coords(block_number)
        string = ""
        for i in xrange(x,x+3):
            for j in xrange(y,y+3):
                string += board[i][j]
        return string
    
    def get_block_coords(self,block_number):
        return {
            0 : (0, 0),
            1 : (0, 3),
            2 : (0, 6),
            3 : (3, 0),
            4 : (3, 3),
            5 : (3, 6),
            6 : (6, 0),
            7 : (6, 3),
            8 : (6, 6),
        }.get(block_number)

    def get_status_of_block(self,block_number,current_block,our_symbol):
        has_completed = True
        first_win=0
        x,y = self.get_block_coords(block_number)
        our_symbol = self.player_symbol
        other_symbol = self.opponent_symbol
        for i in xrange(x,x+3):
            for j in xrange(y,y+3):
                if not (current_block[i][j] == other_symbol or current_block[i][j] == our_symbol):
                    has_completed = False
        if current_block[x][y] == our_symbol and current_block[x + 1][y] == our_symbol and current_block[x + 2][y] == our_symbol:
            if first_win==0:
                first_win=1
        elif current_block[x][y + 1] == our_symbol and current_block[x + 1][y + 1] == our_symbol and current_block[x + 2][y + 1] == our_symbol:
            if first_win==0:
                first_win=1
        elif current_block[x][y + 2] == our_symbol and current_block[x + 1][y + 2] == our_symbol and current_block[x + 2][y + 2] == our_symbol:
            if first_win==0:
                first_win=1
        elif current_block[x][y] == our_symbol and current_block[x][y + 1] == our_symbol and current_block[x][y + 2] == our_symbol:
            if first_win==0:
                first_win=1
        elif current_block[x + 1][y] == our_symbol and current_block[x + 1][y + 1] == our_symbol and current_block[x + 1][y + 2] == our_symbol:
            if first_win==0:
                first_win=1
        elif current_block[x + 2][y] == our_symbol and current_block[x + 2][y + 1] == our_symbol and current_block[x + 2][y + 2] == our_symbol:
            if first_win==0:
                first_win=1
        elif current_block[x][y] == our_symbol and current_block[x + 1][y + 1] == our_symbol and current_block[x + 2][y + 2] == our_symbol:
            if first_win==0:
                first_win=1
        elif current_block[x + 2][y] == our_symbol and current_block[x + 1][y + 1] == our_symbol and current_block[x][y + 2] == our_symbol:
            if first_win==0:
                first_win=1
        if current_block[x][y] == other_symbol and current_block[x + 1][y] == other_symbol and current_block[x + 2][y] == other_symbol:
            if first_win==0:
                first_win=-1
        elif current_block[x][y + 1] == other_symbol and current_block[x + 1][y + 1] == other_symbol and current_block[x + 2][y + 1] == other_symbol:
            if first_win==0:
                first_win=-1
        elif current_block[x][y + 2] == other_symbol and current_block[x + 1][y + 2] == other_symbol and current_block[x + 2][y + 2] == other_symbol:
            if first_win==0:
                first_win=-1
        elif current_block[x][y] == other_symbol and current_block[x][y + 1] == other_symbol and current_block[x][y + 2] == other_symbol:
            if first_win==0:
                first_win=-1
        elif current_block[x + 1][y] == other_symbol and current_block[x + 1][y + 1] == other_symbol and current_block[x + 1][y + 2] == other_symbol:
            if first_win==0:
                first_win=-1
        elif current_block[x + 2][y] == other_symbol and current_block[x + 2][y + 1] == other_symbol and current_block[x + 2][y + 2] == other_symbol:
            if first_win==0:
                first_win=-1
        elif current_block[x][y] == other_symbol and current_block[x + 1][y + 1] == other_symbol and current_block[x + 2][y + 2] == other_symbol:
            if first_win==0:
                first_win=-1
        elif current_block[x + 2][y] == other_symbol and current_block[x + 1][y + 1] == other_symbol and current_block[x][y + 2] == other_symbol:
            if first_win==0:
                first_win=-1
        return (has_completed,first_win)

    def get_permitted_blocks(self,old_move):
        for_corner = [ 0, 2, 3, 5, 6, 8 ]
        blocks_allowed  = []
        if old_move[0] in for_corner and old_move[1] in for_corner:
            if old_move[0] % 3 == 0 and old_move[1] % 3 == 0:
                blocks_allowed = [0, 1, 3]
            elif old_move[0] % 3 == 0 and old_move[1] in [2, 5, 8]:
                blocks_allowed = [1,2,5]
            elif old_move[0] in [2,5, 8] and old_move[1] % 3 == 0:
                blocks_allowed  = [3,6,7]
            elif old_move[0] in [2,5,8] and old_move[1] in [2,5,8]:
                blocks_allowed = [5,7,8]
        else:
            if old_move[0] % 3 == 0 and old_move[1] in [1,4,7]:
                blocks_allowed = [1]
            elif old_move[0] in [1,4,7] and old_move[1] % 3 == 0:
                blocks_allowed = [3]    
            elif old_move[0] in [2,5,8] and old_move[1] in [1,4,7]:
                blocks_allowed = [7]
            elif old_move[0] in [1,4,7] and old_move[1] in [2,5,8]:
                blocks_allowed = [5]
            elif old_move[0] in [1,4,7] and old_move[1] in [1,4,7]:
                blocks_allowed = [4]
        for i in reversed(blocks_allowed):
            if self.status_board[i] != '-':
                blocks_allowed.remove(i)
        return blocks_allowed

    def get_empty_out_of(self,blal):
        cells = []
        for idb in blal:
            id1 = idb/3
            id2 = idb%3
            for i in range(id1*3,id1*3+3):
                for j in range(id2*3,id2*3+3):
                    if self.actual_board[i][j] == '-':
                        cells.append((i,j))
        if cells == []:
            for i in range(9):
                for j in range(9):
                    no = (i/3)*3
                    no += (j/3)
                    if self.actual_board[i][j] == '-' and self.status_board[no] == '-':
                        cells.append((i,j)) 
        return cells

    def game_completed(self,current_board,our_symbol):
        q = [0 for x in xrange(0,9)]
        w = [0 for x in xrange(0,9)]
        j=0
        for i in xrange(0,9):
            q[i],w[i]=self.get_status_of_block(i,current_board,our_symbol)
        for i in xrange(0,9):
            if q[i]==True or w[i]!=0:
                j += 1
        if w[1]+w[2]+w[0]==3 or w[3]+w[4]+w[5]==3 or w[6]+w[7]+w[8]==3 or w[0]+w[3]+w[6]==3 or w[1]+w[4]+w[7]==3 or w[2]+w[5]+w[8]==3 or w[0]+w[5]+w[8]==3 or w[2]+w[5]+w[7]==3:
            return (j,10)
        elif w[1]+w[2]+w[0]==-3 or w[3]+w[4]+w[5]==-3 or w[6]+w[7]+w[8]==-3 or w[0]+w[3]+w[6]==-3 or w[1]+w[4]+w[7]==-3 or w[2]+w[5]+w[8]==-3 or w[0]+w[5]+w[8]==-3 or w[2]+w[5]+w[7]==-3:
            return (j,-10)
        else:
            return (j,0)

    def get_board_status(self):
        return self.get_status_block(0, self.status_board, self.player_symbol)

    def bind_symbol(self,our_symbol):
        self.player_symbol = our_symbol
        self.opponent_symbol = 'x'
        if self.player_symbol == self.opponent_symbol:
            self.opponent_symbol = 'o'
    
    def get_move_from_number(self,block_number,move_number):
        x,y = self.get_block_coords(block_number)
        a,b = self.get_block_coords(move_number) # Just got very lazy there. :)
        return ((x + (a/3)), (y + (b/3)))

    def copy_current_board_elems(self,current_board,board_stat):
        self.actual_board = current_board[:]
        self.status_board = board_stat[:]

    def return_random_move(self,possible_moves):
        return random.choice(possible_moves)

    def make_minimax_saved_move(self,current_board,blocks_allowed,cells):
        acc_moves = []
        for block_number in blocks_allowed:
            string = self.make_block_str(current_board,block_number)
            try:
                move_number = self.heuristic_minimax_table[string]
                cell = self.get_move_from_number(block_number,move_number)
                if cell in cells:
                    acc_moves.append(cell)
            except:
                pass
        try:
            return random.choice(acc_moves)
        except:
            return random.choice(cells)

    def reverse_board_status(self):
        self.status_board = self.backup_status_board[:]

    def heuristic_score(self,board):
        winnable_x = [8,8,8,8,8,8,8,8,8]
        lines_x = [[1,1,1,1,1,1,1,1],[1,1,1,1,1,1,1,1],[1,1,1,1,1,1,1,1],[1,1,1,1,1,1,1,1],
        [1,1,1,1,1,1,1,1],[1,1,1,1,1,1,1,1],[1,1,1,1,1,1,1,1],[1,1,1,1,1,1,1,1],[1,1,1,1,1,1,1,1]]
        winnable_o = [8,8,8,8,8,8,8,8,8]
        lines_o = [[1,1,1,1,1,1,1,1],[1,1,1,1,1,1,1,1],[1,1,1,1,1,1,1,1],[1,1,1,1,1,1,1,1],
        [1,1,1,1,1,1,1,1],[1,1,1,1,1,1,1,1],[1,1,1,1,1,1,1,1],[1,1,1,1,1,1,1,1],[1,1,1,1,1,1,1,1]]
        for index in xrange(9):
            block_coords = self.get_block_coords(index)
            x = block_coords[0]
            y = block_coords[1]
            if board[x][y] == 'x':
                if lines_o[0][0] == 1:
                    lines_o[0][0] = 0
                    winnable_o[index] -= 1
                if lines_o[0][3] == 1:
                    lines_o[0][3] = 0
                    winnable_o[index] -= 1
                if lines_o[0][6] == 1:
                    lines_o[0][6] = 0
                    winnable_o[index] -= 1
            elif board[x][y] == 'o':
                if lines_x[0][0] == 1:
                    lines_x[0][0] = 0
                    winnable_x[index] -= 1
                if lines_x[0][3] == 1:
                    lines_x[0][3] = 0
                    winnable_x[index] -= 1
                if lines_x[0][6] == 1:
                    lines_x[0][6] = 0
                    winnable_x[index] -= 1
            if board[x+2][y] == 'x':
                if lines_o[0][0] == 1:
                    lines_o[0][0] = 0
                    winnable_o[index] -= 1
                if lines_o[0][5] == 1:
                    lines_o[0][5] = 0
                    winnable_o[index] -= 1
                if lines_o[0][7] == 1:
                    lines_o[0][7] = 0
                    winnable_o[index] -= 1
            elif board[x+2][y] == 'o':
                if lines_x[0][0] == 1:
                    lines_x[0][0] = 0
                    winnable_x[index] -= 1
                if lines_x[0][5] == 1:
                    lines_x[0][5] = 0
                    winnable_x[index] -= 1
                if lines_x[0][7] == 1:
                    lines_x[0][7] = 0
                    winnable_x[index] -= 1
            if board[x][y+2] == 'x':
                if lines_o[0][2] == 1:
                    lines_o[0][2] = 0
                    winnable_o[index] -= 1
                if lines_o[0][3] == 1:
                    lines_o[0][3] = 0
                    winnable_o[index] -= 1
                if lines_o[0][7] == 1:
                    lines_o[0][7] = 0
                    winnable_o[index] -= 1
            elif board[x][y+2] == 'o':
                if lines_x[0][2] == 1:
                    lines_x[0][2] = 0
                    winnable_x[index] -= 1
                if lines_x[0][3] == 1:
                    lines_x[0][3] = 0
                    winnable_x[index] -= 1
                if lines_x[0][7] == 1:
                    lines_x[0][7] = 0
                    winnable_x[index] -= 1
            if board[x+2][y+2] == 'x':
                if lines_o[0][2] == 1:
                    lines_o[0][2] = 0
                    winnable_o[index] -= 1
                if lines_o[0][5] == 1:
                    lines_o[0][5] = 0
                    winnable_o[index] -= 1
                if lines_o[0][6] == 1:
                    lines_o[0][6] = 0
                    winnable_o[index] -= 1
            elif board[x+2][y+2] == 'o':
                if lines_x[0][2] == 1:
                    lines_x[0][2] = 0
                    winnable_x[index] -= 1
                if lines_x[0][5] == 1:
                    lines_x[0][5] = 0
                    winnable_x[index] -= 1
                if lines_x[0][6] == 1:
                    lines_x[0][6] = 0
                    winnable_x[index] -= 1
            if board[x+1][y] == 'x':
                if lines_o[0][0] == 1:
                    lines_o[0][0] = 0
                    winnable_o[index] -= 1
                if lines_o[0][4] == 1:
                    lines_o[0][4] = 0
                    winnable_o[index] -= 1
            elif board[x+1][y] == 'o':
                if lines_x[0][0] == 1:
                    lines_x[0][0] = 0
                    winnable_x[index] -= 1
                if lines_x[0][4] == 1:
                    lines_x[0][4] = 0
                    winnable_x[index] -= 1
            if board[x][y+1] == 'x':
                if lines_o[0][1] == 1:
                    lines_o[0][1] = 0
                    winnable_o[index] -= 1
                if lines_o[0][3] == 1:
                    lines_o[0][3] = 0
                    winnable_o[index] -= 1
            elif board[x][y+1] == 'o':
                if lines_x[0][1] == 1:
                    lines_x[0][1] = 0
                    winnable_x[index] -= 1
                if lines_x[0][3] == 1:
                    lines_x[0][3] = 0
                    winnable_x[index] -= 1
            if board[x+2][y+1] == 'x':
                if lines_o[0][1] == 1:
                    lines_o[0][1] = 0
                    winnable_o[index] -= 1
                if lines_o[0][5] == 1:
                    lines_o[0][5] = 0
                    winnable_o[index] -= 1
            elif board[x+2][y+1] == 'o':
                if lines_x[0][1] == 1:
                    lines_x[0][1] = 0
                    winnable_x[index] -= 1
                if lines_x[0][5] == 1:
                    lines_x[0][5] = 0
                    winnable_x[index] -= 1
            if board[x+1][y+2] == 'x':
                if lines_o[0][2] == 1:
                    lines_o[0][2] = 0
                    winnable_o[index] -= 1
                if lines_o[0][4] == 1:
                    lines_o[0][4] = 0
                    winnable_o[index] -= 1
            elif board[x+1][y+2] == 'o':
                if lines_x[0][2] == 1:
                    lines_x[0][2] = 0
                    winnable_x[index] -= 1
                if lines_x[0][4] == 1:
                    lines_x[0][4] = 0
                    winnable_x[index] -= 1
            #Center
            if board[x+1][y+1] == 'x':
                if lines_o[0][1] == 1:
                    lines_o[0][1] = 0
                    winnable_o[index] -= 1
                if lines_o[0][4] == 1:
                    lines_o[0][4] = 0
                    winnable_o[index] -= 1
                if lines_o[0][6] == 1:
                    lines_o[0][6] = 0
                    winnable_o[index] -= 1
                if lines_o[0][7] == 1:
                    lines_o[0][7] = 0
                    winnable_o[index] -= 1
            elif board[x+1][y+1] == 'o':
                if lines_x[0][1] == 1:
                    lines_x[0][1] = 0
                    winnable_x[index] -= 1
                if lines_x[0][4] == 1:
                    lines_x[0][4] = 0
                    winnable_x[index] -= 1
                if lines_x[0][6] == 1:
                    lines_x[0][6] = 0
                    winnable_x[index] -= 1
                if lines_x[0][7] == 1:
                    lines_x[0][7] = 0
                    winnable_x[index] -= 1
        h_list = []
        for index in xrange(9):
            h_list.append( winnable_x[index] - winnable_o[index] )
        winnable_X = 8 #Winnable lines for X on bigger board
        winnable_O = 8 #Winnable lines for O on bigger board
        for index in xrange(9):
            if index in [0,2,6,8]:
                if h_list[index] > 0:
                    winnable_O -= 3
                elif h_list[index] < 0:
                    winnable_X -= 3
            elif index in [1,3,5,7]:
                if h_list[index] > 0:
                    winnable_O -= 2
                elif h_list[index] < 0:
                    winnable_X -= 2
            else:
                if h_list[index] > 0:
                    winnable_O -= 4
                elif h_list[index] < 0:
                    winnable_X -= 4
        H = winnable_X - winnable_O
        return H

    def update_and_save_board_status(self,move_ret,symbol):
        self.backup_status_board = self.status_board[:]
        block_no = (move_ret[0]/3)*3 + (move_ret[1])/3
        id1 = block_no/3
        id2 = block_no%3
        mg = 0
        mflg = 0
        if self.status_board[block_no] == '-':
            if self.actual_board[id1*3][id2*3] == self.actual_board[id1*3+1][id2*3+1] and self.actual_board[id1*3+1][id2*3+1] == self.actual_board[id1*3+2][id2*3+2] and self.actual_board[id1*3+1][id2*3+1] != '-':
                mflg=1
            if self.actual_board[id1*3+2][id2*3] == self.actual_board[id1*3+1][id2*3+1] and self.actual_board[id1*3+1][id2*3+1] == self.actual_board[id1*3][id2*3 + 2] and self.actual_board[id1*3+1][id2*3+1] != '-':
                mflg=1
            if mflg != 1:
                for i in range(id2*3,id2*3+3):
                    if self.actual_board[id1*3][i]==self.actual_board[id1*3+1][i] and self.actual_board[id1*3+1][i] == self.actual_board[id1*3+2][i] and self.actual_board[id1*3][i] != '-':
                        mflg = 1
                        break
            if mflg != 1:
                for i in range(id1*3,id1*3+3):
                    if self.actual_board[i][id2*3]==self.actual_board[i][id2*3+1] and self.actual_board[i][id2*3+1] == self.actual_board[i][id2*3+2] and self.actual_board[i][id2*3] != '-':
                        mflg = 1
                        break
        if mflg == 1:
            self.status_board[block_no] = symbol
        id1 = block_no/3
        id2 = block_no%3
        cells = []
        for i in range(id1*3,id1*3+3):
            for j in range(id2*3,id2*3+3):
                if self.actual_board[i][j] == '-':
                    cells.append((i,j))
        if cells == [] and mflg != 1:
            self.status_board[block_no] = 'd'

    def _get_symbol_from_is_maximizing_player(self, is_maximizing_player):
        if is_maximizing_player:
            return self.player_symbol
        else:
            return self.opponent_symbol

    def perform_heuristic(self,cell):
    	x,y = cell
    	self.actual_board[x][y] = self._get_symbol_from_is_maximizing_player(self.is_max_player)
    	rv = self.heuristic_score(self.actual_board)
    	self.actual_board[x][y] = "-"
    	return rv

    def negamax_alpha_beta_transposition_table(self, opponent_move, depth, alpha, beta, is_maximizing_player):
    	self.is_max_player = is_maximizing_player
        alpha_orig = alpha
        blocks_allowed = self.get_permitted_blocks(opponent_move)
        cells = self.get_empty_out_of(blocks_allowed)
        if not cells:
            if is_maximizing_player:
                return (None, -99999)
            else:
                return (None, 99999)
        board_str = self.make_board_str()
        try:
            tt_depth,tt_flag,tt_value,tt_cell  = self.transposition_table[board_str]
            if tt_depth >= depth:
                if tt_flag == 0:
                    return (tt_cell,tt_value)
                elif tt_flag == -1:
                    alpha = max(alpha,tt_value)
                elif tt_flag == 1: 
                    beta = min(beta,tt_value)
                if alpha >= beta:
                    return (tt_cell,tt_value)
        except:
            pass
        game_status, game_score = self.game_completed(self.actual_board, self._get_symbol_from_is_maximizing_player(is_maximizing_player))
        if depth == 0 and is_maximizing_player:
            return (None, self.heuristic_score(self.actual_board))
        if depth == 0 and not is_maximizing_player:
            return (None, -self.heuristic_score(self.actual_board))
        elif game_status == 9:
            return (None, game_score)
        if is_maximizing_player:    
            v = -99999
        else:
            v = 99999
        cells.sort(key=self.perform_heuristic)
        selected_cell = cells[0]
        for cell in cells:
            x,y = cell
            self.actual_board[x][y] = self._get_symbol_from_is_maximizing_player(is_maximizing_player)
            self.update_and_save_board_status(cell, self._get_symbol_from_is_maximizing_player(is_maximizing_player))
            child_node_values = self.negamax_alpha_beta_transposition_table(cell, depth - 1, -beta, -alpha, (not is_maximizing_player))
            self.actual_board[x][y] = '-'
            self.reverse_board_status()
            old_v = v
            v = max(v, -1*child_node_values[1])
            if v != old_v:
                selected_cell = cell
            alpha = max(alpha,v)
            if beta <= alpha:
                break
        new_entry_value = v
        if new_entry_value <= alpha_orig:
            new_entry_flag = 1 
        elif new_entry_value >= beta:
            new_entry_flag = -1 
        else:
            new_entry_flag = 0
        new_entry_depth = depth
        self.transposition_table[board_str] = (new_entry_depth,new_entry_flag,new_entry_value,selected_cell)
        return (selected_cell, v) 

    def move(self,current_board,board_stat,opponent_move,our_symbol):
        self.bind_symbol(our_symbol)
        self.copy_current_board_elems(current_board,board_stat)
        self.number_of_moves = self.number_of_moves + 1

        blocks_allowed = self.get_permitted_blocks(opponent_move)
        cells = self.get_empty_out_of(blocks_allowed)

        if self.number_of_moves < 8:
            depth = 3
        elif self.number_of_moves < 16:
            depth = 5
        else:
            depth = 7
        signal.signal(signal.SIGALRM, EnforcedTimeHandler)
        signal.alarm(ENFORCED_TIME)
        try:
            move, value = self.negamax_alpha_beta_transposition_table(opponent_move, depth, -99999, 99999, True)
        except EnforcedTimeExecption:
            move = self.make_minimax_saved_move(current_board,blocks_allowed,cells)
        signal.alarm(0)
        if move not in cells:
            move = random.choice(cells)
        print self.player_symbol
        return move
