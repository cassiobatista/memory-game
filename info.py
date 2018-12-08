import os

DEGUB = False

CARDS_DIR = os.path.join('.', 'cards')
BOARD_ROWS = 3 
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

WINDOW_TITLE = \
	u'Memory Game in Python 3!'

INFO =  WINDOW_TITLE + '<br>' \
		u'<br>' + \
		u'Author(s):' + \
		u'<br>' + \
		u'Cassio Trindade Batista' + \
		u'<br><br>' + \
		u'Contact:' + \
		u'<br>' + \
		u'<a href=mailto:cassio.batista.13@gmail.com>cassio.batista.13@gmail.com</a>' + \
		u'<br><br>' + \
		u'Copyleft 2018' + \
		u'<br>' + \
		u'Visualization, Interaction and Intelligent Systems Lab' + \
		u'<br>' + \
		u'Institute of Exact and Natural Sciences' + \
		u'<br>' + \
		u'Federal University of Pará' + \
		u'<br>' + \
		u'Belém, Brazil'

