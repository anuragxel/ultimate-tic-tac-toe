import random

class Player(object):
	'''
		Player Class Container.
	'''
	def __init__(self):
		self.number_of_moves = 0
		self.player_symbol = None
		self.opponent_symbol = None
		self.actual_board = [[]]
		self.status_board = []

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
		x,y = 0,0	
		x,y = get_block_coords(block_number)

		for i in xrange(x,x+3):
			for j in xrange(y,y+3):
				if current_block[x][y] == other_symbol or current_block[x][y] == our_symbol:
					has_completed = True

		if current_block[x][y] == our_symbol and current_block[x + 1][y] == our_symbol and current_block[x + 2][y] == our_symbol:
			has_won = True
		elif current_block[x][y + 1] == our_symbol and current_block[x + 1][y + 1] == our_symbol and current_block[x + 2][y + 1] == our_symbol:
			has_won = True
		elif current_block[x][y + 2] == our_symbol and current_block[x + 1][y + 2] == our_symbol and current_block[x + 2][y + 2] == our_symbol:
			has_won = True
		elif current_block[x][y] == our_symbol and current_block[x][y + 1] == our_symbol and current_block[x][y + 2] == our_symbol:
			has_won = True
		elif current_block[x + 1][y] == our_symbol and current_block[x + 1][y + 1] == our_symbol and current_block[x + 1][y + 2] == our_symbol:
			has_won = True
		elif current_block[x + 2][y] == our_symbol and current_block[x + 2][y + 1] == our_symbol and current_block[x + 2][y + 2] == our_symbol:
			has_won = True
		elif current_block[x][y] == our_symbol and current_block[x + 1][y + 1] == our_symbol and current_block[x + 2][y + 2] == our_symbol:
			has_won = True
		elif current_block[x + 2][y] == our_symbol and current_block[x + 1][y + 1] == our_symbol and current_block[x][y + 2] == our_symbol:
			has_won = True
		
		if current_block[x][y] == other_symbol and current_block[x + 1][y] == other_symbol and current_block[x + 2][y] == other_symbol:
			has_lost = True
		elif current_block[x][y + 1] == other_symbol and current_block[x + 1][y + 1] == other_symbol and current_block[x + 2][y + 1] == other_symbol:
			has_lost = True
		elif current_block[x][y + 2] == other_symbol and current_block[x + 1][y + 2] == other_symbol and current_block[x + 2][y + 2] == other_symbol:
			has_lost = True
		elif current_block[x][y] == other_symbol and current_block[x][y + 1] == other_symbol and current_block[x][y + 2] == other_symbol:
			has_lost = True
		elif current_block[x + 1][y] == other_symbol and current_block[x + 1][y + 1] == other_symbol and current_block[x + 1][y + 2] == other_symbol:
			has_lost = True
		elif current_block[x + 2][y] == other_symbol and current_block[x + 2][y + 1] == other_symbol and current_block[x + 2][y + 2] == other_symbol:
			has_lost = True
		elif current_block[x][y] == other_symbol and current_block[x + 1][y + 1] == other_symbol and current_block[x + 2][y + 2] == other_symbol:
			has_lost = True
		elif current_block[x + 2][y] == other_symbol and current_block[x + 1][y + 1] == other_symbol and current_block[x][y + 2] == other_symbol:
			has_lost = True
		return (has_won, has_lost, has_completed)

	def tell_permitted_blocks(self,opponent_move):
		'''
		Parameters - opponent_move <(a,b)>
		return value - blocks_allowed <[]>
		'''
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

	def get_baseline_allowed_moves(self,current_board,permitted_blocks,our_symbol):
		pass

	def return_random_move(self,possible_moves):
		return random.choice(possible_moves)

	def is_board_won(self):
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
		print "flag "  + flag
		mvp = raw_input()
		mvp = mvp.split()
		self.number_of_moves += 1
		return current_move
