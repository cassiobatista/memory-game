import os

DEGUB = False

CARDS_DIR = os.path.join('.', 'cards')
BOARD_SIZE = 4 # an even number is required
NUM_CARDS  = BOARD_SIZE**2//2

assert BOARD_SIZE > 0, 'board dimensions must be a positive number, asshole'
assert BOARD_SIZE**2 % 2 == 0, 'board dimensions must be even, dumbass'

HOVER_FOCUS = \
	'QPushButton::focus { '   + \
	'    background: black; ' + \
	'    color: white; '      + \
	'}'

WIN_MSG = \
	u'Parabéns, você ganhou.'
