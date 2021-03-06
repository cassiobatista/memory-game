import os

DEGUB = False
PT_BR = False

ICONS_DIR      = os.path.join('.', 'icons')
RESOURCES_DIR  = os.path.join('.', 'res')

BOARD_ROWS = 3 
BOARD_COLS = 4
NUM_CARDS  = BOARD_COLS * BOARD_ROWS // 2

assert BOARD_COLS*BOARD_ROWS > 0, \
			u'as dimensões do tabuleiro devem ser positivas, trouxa' if PT_BR else \
			u'board dimensions must be positive, asshole' 
assert BOARD_COLS*BOARD_ROWS % 2 == 0, \
			u'as dimensões devem ser pares, retardado' if PT_BR else \
			u'board dimensions must be even, dumbass'

HOVER_FOCUS = \
	'QPushButton::focus { '   + \
	'    background: black; ' + \
	'    color: white; '      + \
	'}'

WIN_MSG = \
	u'Parabéns, você ganhou!' if PT_BR else \
	u'Congratulations, you win!'

WINDOW_TITLE = \
	u'Jogo da Memória em Python 3!' if PT_BR else \
	u'Memory Game in Python 3!'

MOUSE_ERROR_MSG = \
	u'Por favor, ao invés de utilizar o mouse, utilize somente o teclado.' if PT_BR else \
	u'Please, do not use the mouse, use only the keyboard instead.'

INFO = WINDOW_TITLE + '<br>' \
		u'<br>' + \
		(u'Autor(es):' if PT_BR else u'Author(s):') + \
		u'<br>' + \
		u'Cassio Trindade Batista' + \
		u'<br><br>' + \
		(u'Contato:' if PT_BR else u'Contact:') + \
		u'<br>' + \
		u'<a href=mailto:cassio.batista.13@gmail.com>cassio.batista.13@gmail.com</a>' + \
		u'<br><br>' + \
		u'Copyleft 2018' + \
		u'<br>' + \
		(u'Lab de Visualização, Interação e Sistemas Inteligentes' if PT_BR else \
		u'Visualization, Interaction and Intelligent Systems Lab') + \
		u'<br>' + \
		(u'Instituto de Ciências Exatas e Naturais' if PT_BR else \
		u'Institute of Exact and Natural Sciences') + \
		u'<br>' + \
		(u'Universidade Federal do Pará' if PT_BR else \
		u'Federal University of Pará') + \
		u'<br>' + \
		(u'Belém, Brasil' if PT_BR else u'Belém, Brazil')

