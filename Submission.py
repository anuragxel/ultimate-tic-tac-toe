class Player(object):
	'''
		Player Class Container.
	'''
	def __init__(self):
		pass

	def init(self): #Py3 Compatiblity
		pass

	def tell_permitted_blocks(opponent_move):
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

	def move(self,current_board,board_stat,opponent_move,flag):
		'''
		Parameters - opponent_move - <(a,b)> previous move by opponent; board_stat - <[]> info of blocks won/lost; 
					current_board - <[]> current board situation; flag - <unused> unknown
		Return Value - move- <(row,column)> 
		'''
		pass