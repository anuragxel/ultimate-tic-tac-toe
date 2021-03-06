import random
import json
import datetime
import signal

ENFORCED_TIME = 5
hrst_table = json.load(open('yay.json'))

class EnforcedTimeExecption(Exception):
    pass

def EnforcedTimeHandler(signum, frame):
        raise EnforcedTimeExecption()

class Player(object):
    '''
        Player Class Container.
    '''
    def __init__(self):
        self.number_of_moves = 0
        self.player_symbol = None
        self.opponent_symbol = None
        self.actual_board = [[]] # '-', 'x', 'o'
        self.status_board = [] # '-', 'x', 'o'
        self.backup_status_board = []
        self.transposition_table = {}
        self.heuristic_minimax_table = hrst_table
        self.prev_time = datetime.datetime.now()

    def init(self):
        self.__init__()

    def make_board_str(self):
        string = ""
        for i in xrange(0,9):
            for j in xrange(0,9):
                string += self.actual_board[i][j]
        return string

    def get_block_coords(self,block_number):
        return {
            0 : (0, 0),
            1 : (3, 0),
            2 : (6, 0),
            3 : (0, 3),
            4 : (3, 3),
            5 : (6, 3),
            6 : (0, 6),
            7 : (3, 6),
            8 : (6, 6),
        }.get(block_number)

    def get_status_of_block(self,block_number,current_block,our_symbol):
        has_completed = False
        first_win=0     #0=none 1=me 2=other
        x,y = self.get_block_coords(block_number)

        our_symbol = self.player_symbol
        other_symbol = self.opponent_symbol

        for i in xrange(x,x+3):
            for j in xrange(y,y+3):
                if not (current_block[x][y] == other_symbol or current_block[x][y] == our_symbol):
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
        for_corner = [0,2,3,5,6,8]

        #List of permitted blocks, based on old move.
        blocks_allowed  = []

        if old_move[0] in for_corner and old_move[1] in for_corner:
            ## we will have 3 representative blocks, to choose from

            if old_move[0] % 3 == 0 and old_move[1] % 3 == 0:
                ## top left 3 blocks are allowed
                blocks_allowed = [0, 1, 3]
            elif old_move[0] % 3 == 0 and old_move[1] in [2, 5, 8]:
                ## top right 3 blocks are allowed
                blocks_allowed = [1,2,5]
            elif old_move[0] in [2,5, 8] and old_move[1] % 3 == 0:
                ## bottom left 3 blocks are allowed
                blocks_allowed  = [3,6,7]
            elif old_move[0] in [2,5,8] and old_move[1] in [2,5,8]:
                ### bottom right 3 blocks are allowed
                blocks_allowed = [5,7,8]
            else:
                print "SOMETHING REALLY WEIRD HAPPENED!"
                sys.exit(1)
        else:
        #### we will have only 1 block to choose from (or maybe NONE of them, which calls for a free move)
            if old_move[0] % 3 == 0 and old_move[1] in [1,4,7]:
                ## upper-center block
                blocks_allowed = [1]
    
            elif old_move[0] in [1,4,7] and old_move[1] % 3 == 0:
                ## middle-left block
                blocks_allowed = [3]
        
            elif old_move[0] in [2,5,8] and old_move[1] in [1,4,7]:
                ## lower-center block
                blocks_allowed = [7]

            elif old_move[0] in [1,4,7] and old_move[1] in [2,5,8]:
                ## middle-right block
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

    def get_baseline_allowed_moves(self,current_board,moves):       #permitted moves(gand bachao)
        pass

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

    def return_random_move(self,possible_moves):
        return random.choice(possible_moves)

    def get_board_status(self):
        return self.get_status_block(0, self.status_board, self.player_symbol)

    def bind_symbol(self,our_symbol):
        self.player_symbol = our_symbol
        self.opponent_symbol = 'x'
        if self.player_symbol == self.opponent_symbol:
            self.opponent_symbol = 'o'
        

    def copy_current_board_elems(self,current_board,board_stat):
        self.actual_board = current_board[:]
        self.status_board = board_stat[:]
    
    def get_move_from_number(block_number,move_number):
        x,y = self.get_block_coords(block_number)
        a,b = self.get_block_coords(move_number) # Just got very lazy there. :)
        return ( x+(a/3), y+(b/3) )

    def make_block_str(self,board,block_number):
        x,y = self.get_block_coords(block_number)
        string = ""
        for i in xrange(x,x+3):
            for j in xrange(y,y+3):
                string += board[i][j]
        return string

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

    def heuristic_score(self,board):
        """
        Computes heuristic_score for the passed board configuration
        """
        #Calculate h values for each small board
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
            #Bad code but can't think of any better atm :/
            #4 corners
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
            #4 sides
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

        #Populate h list
        h_list = []
        for index in xrange(9):
            h_list.append( winnable_x[index] - winnable_o[index] )
        #Calculate H using h values
        winnable_X = 8 #Winnable lines for X on bigger board
        winnable_O = 8 #Winnable lines for O on bigger board
        for index in xrange(9):
            if index in [0,2,6,8]:
                #Corner
                if h_list[index] > 0:
                    winnable_O -= 3
                elif h_list[index] < 0:
                    winnable_X -= 3
            elif index in [1,3,5,7]:
                #Side
                if h_list[index] > 0:
                    winnable_O -= 2
                elif h_list[index] < 0:
                    winnable_X -= 2
            else:
                #Center
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

    def reverse_board_status(self):
        self.status_board = self.backup_status_board[:]

    def free_move(self):
        pass # return whatever

    def _get_symbol_from_is_maximizing_player(self, is_maximizing_player):
        if is_maximizing_player:
            return self.player_symbol
        else:
            return self.opponent_symbol

    def negamax_alpha_beta_transposition_table(self, opponent_move, depth, alpha, beta, is_maximizing_player):
        alpha_orig = alpha
        blocks_allowed = self.get_permitted_blocks(opponent_move)
        cells = self.get_empty_out_of(blocks_allowed)
        if not cells:
            if is_maximizing_player:
                return (None, -99999)
            else:
                return (None, 99999)
        # Table lookup here
        board_str = self.make_board_str()
        try:
            tt_depth,tt_flag,tt_value  = self.transposition_table[board_str]
            if tt_depth >= depth:
                if tt_flag == 0: # EXACT
                    return (cells[0],tt_value)
                elif tt_flag == -1: #LOWERBOUND
                    alpha = max(alpha,tt_value)
                elif tt_flag == 1: #UPPERBOUND
                    beta = min(beta,tt_value)
                if alpha >= beta:
                    return (cells[0],tt_value)
        except:
            pass
        # check termination conditions
        game_status, game_score = self.game_completed(self.actual_board, self._get_symbol_from_is_maximizing_player(is_maximizing_player))
        if depth == 0 and is_maximizing_player: # Or is terminal node
            return ((cells[0]), self.heuristic_score(self.actual_board))
        if depth == 0 and not is_maximizing_player:
            return ((cells[0]), -self.heuristic_score(self.actual_board))
        elif game_status == 9:
            return ((cells[0]), game_score)
        if is_maximizing_player:    
            v = -99999 # for the first case only
        else:
            v = 99999
        for cell in cells:
            x,y = cell
            self.actual_board[x][y] = self._get_symbol_from_is_maximizing_player(is_maximizing_player)
            self.update_and_save_board_status(cell, self._get_symbol_from_is_maximizing_player(is_maximizing_player))
            child_node_values = self.negamax_alpha_beta_transposition_table(cell, depth - 1, -beta, -alpha, (not is_maximizing_player))
            self.actual_board[x][y] = '-'
            self.reverse_board_status()
            v = -1*child_node_values[1]
            if v > alpha:
                alpha = v
            if beta <= alpha:
                break
        # Building States here
        new_entry_value = v
        if new_entry_value <= alpha_orig:
            new_entry_flag = 1 #UPPERBOUND
        elif new_entry_value >= beta:
            new_entry_flag = -1 #LOWERBOUND
        else:
            new_entry_flag = 0 # EXACT
        new_entry_depth = depth
        self.transposition_table[board_str] = (new_entry_depth,new_entry_flag,new_entry_value)
        return (cells[0], v) # return the cell of the calling function 


    def negamax_alpha_beta(self, opponent_move, depth, alpha, beta, is_maximizing_player):
        blocks_allowed = self.get_permitted_blocks(opponent_move)
        cells = self.get_empty_out_of(blocks_allowed)
        # check termination conditions
        if not cells:
            if is_maximizing_player:
                return (None, -99999)
            else:
                return (None, 99999)
        game_status, game_score = self.game_completed(self.actual_board, self._get_symbol_from_is_maximizing_player(is_maximizing_player))
        
        if depth == 0 and is_maximizing_player: # Or is terminal node
            return ((cells[0]), self.heuristic_score(self.actual_board))
        if depth == 0 and not is_maximizing_player:
            return ((cells[0]), -self.heuristic_score(self.actual_board))

        elif game_status == 9:
            return ((cells[0]), game_score)
        if is_maximizing_player:    
            v = -99999 # for the first case only
        else:
            v = 99999
        for cell in cells:
            x,y = cell
            self.actual_board[x][y] = self._get_symbol_from_is_maximizing_player(is_maximizing_player)
            self.update_and_save_board_status(cell, self._get_symbol_from_is_maximizing_player(is_maximizing_player))
            child_node_values = self.negamax_alpha_beta(cell, depth - 1, -beta, -alpha, (not is_maximizing_player))
            self.actual_board[x][y] = '-'
            self.reverse_board_status()
            v = -1*child_node_values[1]
            if v > alpha:
                alpha = v
            if beta <= alpha:
                break
        return (cells[0], v) # return the cell of the calling function 
    
    # """
    def minimax_alpha_beta_transposition_table(self, opponent_move, depth, alpha, beta, is_maximizing_player):
        highest_heurestic = 0
        cell_selected = None

        alpha_orig = alpha
        board_str = self.make_board_str()
        try:
            tt_depth,tt_flag,tt_value  = self.transposition_table[board_str]
            if tt_depth >= depth:
                if tt_flag == 0: # EXACT
                    return (cells[0],tt_value)
                elif tt_flag == -1: #LOWERBOUND
                    alpha = max(alpha,tt_value)
                elif tt_flag == 1: #UPPERBOUND
                    beta = min(beta,tt_value)
                if alpha >= beta:
                    return (cells[0],tt_value)
        except:
            pass
        blocks_allowed = self.get_permitted_blocks(opponent_move)
        cells = self.get_empty_out_of(blocks_allowed)
        # check termination conditions
        if not cells:
            if is_maximizing_player:
                return (None, -99999)
            else:
                return (None, 99999)
        # Table lookup here

        game_status, game_score = self.game_completed(self.actual_board, self._get_symbol_from_is_maximizing_player(is_maximizing_player))
        if depth == 0: # Or is terminal node
            return ((cells[0]), self.heuristic_score(self.actual_board))
        elif game_status == 9:
            return ((cells[0]), game_score)
        else:
            # begin to prune
            if is_maximizing_player:
                v = -99999 # for the first case only
                for cell in cells:
                    x,y = cell
                    self.actual_board[x][y] = self._get_symbol_from_is_maximizing_player(is_maximizing_player)
                    self.update_and_save_board_status(cell, self._get_symbol_from_is_maximizing_player(is_maximizing_player))
                    temp = self.minimax_alpha_beta_transposition_table(cell, depth - 1, alpha, beta, False)
                    v = max(v, temp[1])
                    self.actual_board[x][y] = '-'
                    self.reverse_board_status()
                    if v > alpha:
                        alpha = v
                    if beta <= alpha:
                        break
                    if highest_heurestic < temp[1]:
                        highest_heurestic = temp[1]
                        cell_selected = temp[0]
            else:
                v = 99999 # for the first case only
                for cell in cells:
                    x,y = cell
                    self.actual_board[x][y] = self._get_symbol_from_is_maximizing_player(is_maximizing_player)
                    self.update_and_save_board_status(cell, self._get_symbol_from_is_maximizing_player(is_maximizing_player))
                    temp = self.minimax_alpha_beta_transposition_table(cell, depth - 1, alpha, beta, True)
                    v= min(v, temp[1])
                    self.actual_board[x][y] = '-'
                    self.reverse_board_status()
                    if beta < v:
                        beta = v
                    if beta <= alpha:
                        break
                    if highest_heurestic < temp[1]:
                        highest_heurestic = temp[1]
                        cell_selected = temp[0]
            # Building States here
            new_entry_value = v
            if new_entry_value <= alpha_orig:
                new_entry_flag = 1 #UPPERBOUND
            elif new_entry_value >= beta:
                new_entry_flag = -1 #LOWERBOUND
            else:
                new_entry_flag = 0 # EXACT
            new_entry_depth = depth
            self.transposition_table[board_str] = (new_entry_depth,new_entry_flag,new_entry_value)
            return (cells[0], v) # return the cell of the calling function

    # """
    def minimax_alpha_beta(self, opponent_move, depth, alpha, beta, is_maximizing_player):
        blocks_allowed = self.get_permitted_blocks(opponent_move)
        cells = self.get_empty_out_of(blocks_allowed)
        # check termination conditions
        if not cells:
            if is_maximizing_player:
                return (None, -99999)
            else:
                return (None, 99999)
        game_status, game_score = self.game_completed(self.actual_board, self._get_symbol_from_is_maximizing_player(is_maximizing_player))
        if depth == 0: # Or is terminal node
            return ((cells[0]), self.heuristic_score(self.actual_board))
        elif game_status == 9:
            return ((cells[0]), game_score)
        else:
            # begin to prune
            if is_maximizing_player:
                v = -99999 # for the first case only
                for cell in cells:
                    x,y = cell
                    self.actual_board[x][y] = self._get_symbol_from_is_maximizing_player(is_maximizing_player)
                    self.update_and_save_board_status(cell, self._get_symbol_from_is_maximizing_player(is_maximizing_player))
                    child_node_values = self.minimax_alpha_beta(cell, depth - 1, alpha, beta, False)
                    self.actual_board[x][y] = '-'
                    self.reverse_board_status()
                    v = child_node_values[1]
                    if v > alpha:
                        alpha = v
                    if beta <= alpha:
                        break
                return (cells[0], v) # return the cell of the calling function 
            else:
                v = 99999 # for the first case only
                for cell in cells:
                    x,y = cell
                    self.actual_board[x][y] = self._get_symbol_from_is_maximizing_player(is_maximizing_player)
                    self.update_and_save_board_status(cell, self._get_symbol_from_is_maximizing_player(is_maximizing_player))
                    child_node_values = self.minimax_alpha_beta(cell, depth - 1, alpha, beta, True)
                    self.actual_board[x][y] = '-'
                    self.reverse_board_status()
                    v = child_node_values[1]
                    if beta < v:
                        beta = v
                    if beta <= alpha:
                        break
                return (cells[0], v) # return the cell of the calling function

    def free_move(self):
        print "Reached free move"
        return None

    def move(self,current_board,board_stat,opponent_move,our_symbol):
        '''
        Parameters - opponent_move - <(a,b)> previous move by opponent; board_stat - <[]> info of blocks won/lost; 
                    current_board - <[]> current board situation; our_symbol
        Return Value - move- <(row,column)> 
        '''
        self.bind_symbol(our_symbol)
        self.copy_current_board_elems(current_board,board_stat)
        self.number_of_moves = self.number_of_moves + 1

        blocks_allowed = self.get_permitted_blocks(opponent_move)
        cells = self.get_empty_out_of(blocks_allowed)

        if not cells:
            return self.free_move()

        if self.number_of_moves < 10:
            print "switching to level 3"
            depth = 3
        elif self.number_of_moves < 18:
            print "switching to level 5"
            depth = 5
        else:
            print "switching to level 7"
            depth = 7

        print self.player_symbol
        signal.signal(signal.SIGALRM, EnforcedTimeHandler)
        signal.alarm(ENFORCED_TIME)
        try:
            move, value = self.minimax_alpha_beta_transposition_table(opponent_move, depth, -99999, 99999, True)
        except EnforcedTimeExecption:
            move = self.make_minimax_saved_move(current_board,blocks_allowed,cells)
            #print "TLE\t\t\t\top: " + str(opponent_move) + "\t\t\t" + str(move) 
        signal.alarm(0)
        if move not in cells:
            return random.choice(cells)
        return move
