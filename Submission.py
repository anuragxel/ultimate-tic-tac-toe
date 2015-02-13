import random

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

	def init(self):
		self.__init__()

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
		has_won = False
		has_lost = False
		has_completed = False
		first_win=0		#0=none 1=me 2=other 
		x,y = get_block_coords(block_number)

		our_symbol = self.player_symbol
		other_symbol = self.opponent_symbol

		for i in xrange(x,x+3):
			for j in xrange(y,y+3):
				if current_block[x][y] == other_symbol or current_block[x][y] == our_symbol:
					has_completed = True

		if current_block[x][y] == our_symbol and current_block[x + 1][y] == our_symbol and current_block[x + 2][y] == our_symbol:
			has_won = True
			if first_win==0
				first_win=1
		elif current_block[x][y + 1] == our_symbol and current_block[x + 1][y + 1] == our_symbol and current_block[x + 2][y + 1] == our_symbol:
			has_won = True
			if first_win==0
				first_win=1
		elif current_block[x][y + 2] == our_symbol and current_block[x + 1][y + 2] == our_symbol and current_block[x + 2][y + 2] == our_symbol:
			has_won = True
			if first_win==0
				first_win=1
		elif current_block[x][y] == our_symbol and current_block[x][y + 1] == our_symbol and current_block[x][y + 2] == our_symbol:
			has_won = True
			if first_win==0
				first_win=1
		elif current_block[x + 1][y] == our_symbol and current_block[x + 1][y + 1] == our_symbol and current_block[x + 1][y + 2] == our_symbol:
			has_won = True
			if first_win==0
				first_win=1
		elif current_block[x + 2][y] == our_symbol and current_block[x + 2][y + 1] == our_symbol and current_block[x + 2][y + 2] == our_symbol:
			has_won = True
			if first_win==0
				first_win=1
		elif current_block[x][y] == our_symbol and current_block[x + 1][y + 1] == our_symbol and current_block[x + 2][y + 2] == our_symbol:
			has_won = True
			if first_win==0
				first_win=1
		elif current_block[x + 2][y] == our_symbol and current_block[x + 1][y + 1] == our_symbol and current_block[x][y + 2] == our_symbol:
			has_won = True
			if first_win==0
				first_win=1
		
		if current_block[x][y] == other_symbol and current_block[x + 1][y] == other_symbol and current_block[x + 2][y] == other_symbol:
			has_lost = True
			if first_win==0
				first_win=-1
		elif current_block[x][y + 1] == other_symbol and current_block[x + 1][y + 1] == other_symbol and current_block[x + 2][y + 1] == other_symbol:
			has_lost = True
			if first_win==0
				first_win=-1
		elif current_block[x][y + 2] == other_symbol and current_block[x + 1][y + 2] == other_symbol and current_block[x + 2][y + 2] == other_symbol:
			has_lost = True
			if first_win==0
				first_win=-1
		elif current_block[x][y] == other_symbol and current_block[x][y + 1] == other_symbol and current_block[x][y + 2] == other_symbol:
			has_lost = True
			if first_win==0
				first_win=-1
		elif current_block[x + 1][y] == other_symbol and current_block[x + 1][y + 1] == other_symbol and current_block[x + 1][y + 2] == other_symbol:
			has_lost = True
			if first_win==0
				first_win=-1
		elif current_block[x + 2][y] == other_symbol and current_block[x + 2][y + 1] == other_symbol and current_block[x + 2][y + 2] == other_symbol:
			has_lost = True
			if first_win==0
				first_win=-1
		elif current_block[x][y] == other_symbol and current_block[x + 1][y + 1] == other_symbol and current_block[x + 2][y + 2] == other_symbol:
			has_lost = True
			if first_win==0
				first_win=-1
		elif current_block[x + 2][y] == other_symbol and current_block[x + 1][y + 1] == other_symbol and current_block[x][y + 2] == other_symbol:
			has_lost = True
			if first_win==0
				first_win=-1
		return (has_completed,first_win)

	def get_permitted_blocks(self,opponent_move):
		blocks_allowed = []
		for_corner = [ 0, 2, 3, 5, 6, 8 ]
		if opponent_move[0] in for_corner and opponent_move[1] in for_corner:
			if opponent_move[0] % 3 == 0 and opponent_move[1] % 3 == 0:
				blocks_allowed = [0, 1, 3]
			elif opponent_move[0] % 3 == 0 and opponent_move[1] in [2, 5, 8]:
				blocks_allowed = [1,2,5]
			elif opponent_move[0] in [2,5, 8] and opponent_move[1] % 3 == 0:
				blocks_allowed  = [3,6,7]
			elif opponent_move[0] in [2,5,8] and opponent_move[1] in [2,5,8]:
				blocks_allowed = [5,7,8]
		else:
			if opponent_move[0] % 3 == 0 and opponent_move[1] in [1,4,7]:
				blocks_allowed = [1]
			elif opponent_move[0] in [1, 4, 7] and opponent_move[1] % 3 == 0:
				blocks_allowed = [3]
			elif opponent_move[0] in [2, 5, 8] and opponent_move[1] in [1, 4, 7]:
				blocks_allowed = [7]
			elif opponent_move[0] in [1, 4, 7] and opponent_move[1] in [2, 5, 8]:
				blocks_allowed = [5]
			elif opponent_move[0] in [1, 4, 7] and opponent_move[1] in [1, 4, 7]:
				blocks_allowed = [4]
		return blocks_allowed

	def get_empty_out_of(self, permitted_blocks):
	gameb = self.current_board
	blal = permitted_blocks
	cells = []
	for idb in blal:
		id1 = idb/3
		id2 = idb%3
		for i in range(id1*3,id1*3+3):
			for j in range(id2*3,id2*3+3):
				if gameb[i][j] == '-':
					cells.append((i,j))
	if cells == []:
		for i in range(9):
			for j in range(9):
				if gameb[i][j] == '-':
					cells.append((i,j))	
	return cells

	def get_baseline_allowed_moves(self,current_board,moves): 		#permitted moves(gand bachao)
		pass

	def return_random_move(self,possible_moves):
		return random.choice(possible_moves)

	def get_board_status(self):
		return self.get_status_block(0, self.status_board, self.player_symbol)

	def bind_symbol(self,our_symbol):
		self.opponent_symbol = 'x'
		if our_symbol == self.opponent_symbol:
			self.opponent_symbol = 'o'
		self.player_symbol = our_symbol

	def copy_current_board_elems(self,current_board,board_stat):
		self.actual_board = current_board[:]
		self.status_board = board_stat[:]

	def move(self,current_board,board_stat,opponent_move,our_symbol):
		'''
		Parameters - opponent_move - <(a,b)> previous move by opponent; board_stat - <[]> info of blocks won/lost; 
					current_board - <[]> current board situation; our_symbol
		Return Value - move- <(row,column)> 
		'''
	#	bind_symbol(our_symbol)
	#	copy_current_board_elems(current_board,board_stat)
	#	mvp = raw_input()
	#	mvp = mvp.split()
	#	self.number_of_moves += 1
	#	return current_move
		blocks_allowed=get_permitted_blocks(opponent_move)
		cells=get_empty_out_of(blocks_allowed)
		game_status,game_score=game_completed(current_board,'x')
		if game_status==9:
			return game_score #-10||0||10
		else:
			alpha=beta=utiity=NULL
			if our_symbol=='x':
				for cell in cells:
					current_board[cell]='x'
					a=move(self,current_board,board_stat,cell,'o')
					current_board[cell]='-'
					if utiity== NULL || utiity<a:
						utiity=a
					if utiity > alpha || alpha == NULL:
						alpha=utiity
					if alpha> beta && beta != NULL:
						break
				return alpha
			elif our_symbol == 'o':
				for cell in cells:
					current_board[cell]='o'
					a=move(self,current_board,board_stat,cell,'x')
					current_board[cell]='-'
					if utiity== NULL || utiity>a:
						utiity=a
					if utiity < beta || alpha == NULL:
						beta=utiity
					if alpha> beta && beta != NULL:
						break
				return beta 


# get_empty_out_of(gameboard, permitted_blocks) returns possible_moves




def game_completed(self,current_board,our_symbol):
	q[]=w[]=0
	j=0
	for i in xrange(0,8):
		q[i],w[i]=get_status_of_block(i,current_block,our_symbol)
	for i in xrange(0,8):
		if q[i]==True || w[i]!=0:
			j++
	if w[1]+w[2]+w[0]==3 || w[3]+w[4]+w[5]==3 || w[6]+w[7]+w[8]==3 || w[0]+w[3]+w[6]==3 || w[1]+w[4]+w[7]==3 || w[2]+w[5]+w[8]==3 ||w[0]+w[5]+w[8]==3 || w[2]+w[5]+w[7]==3:
		return (j,10)
	elif w[1]+w[2]+w[0]==-3 || w[3]+w[4]+w[5]==-3 || w[6]+w[7]+w[8]==-3 || w[0]+w[3]+w[6]==-3 || w[1]+w[4]+w[7]==-3 || w[2]+w[5]+w[8]==-3 ||w[0]+w[5]+w[8]==-3 || w[2]+w[5]+w[7]==-3:
		return (j,-10)
	else:
		return (j,0)

