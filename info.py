import os

DEGUB = False

CARDS_DIR = os.path.join('.', 'cards')
BOARD_ROWS = 2 
BOARD_COLS = 4
NUM_CARDS    = BOARD_COLS*BOARD_ROWS//2

assert BOARD_COLS*BOARD_ROWS > 0, 'board dimensions must be a positive number, asshole'
assert BOARD_COLS*BOARD_ROWS % 2 == 0, 'board dimensions must be even, dumbass'

HOVER_FOCUS = \
	'QPushButton::focus { '   + \
	'    background: black; ' + \
	'    color: white; '      + \
	'}'

WIN_MSG = \
	u'Parabéns, você ganhou.'
