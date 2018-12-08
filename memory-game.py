#!/usr/bin/env python3
# https://stackoverflow.com/questions/20856518/navigate-between-widgets-using-arrows-in-qt
# https://github.com/sromku/memory-game
#
# author: nov 2018
# Cassio Batista - cassio.batista.13@gmail.com

import sys
import os
import time
import numpy as np

from collections import deque
from PyQt5 import QtWidgets, QtGui, QtCore
from termcolor import colored

import info

class Card(QtWidgets.QPushButton):
	def __init__(self, icon_index, face_icon_path, back_icon_path):
		super(Card, self).__init__()
		self.face_icon = QtGui.QIcon(QtGui.QPixmap(face_icon_path))
		self.back_icon = QtGui.QIcon(QtGui.QPixmap(back_icon_path))

		self.icon_index  = icon_index
		self.pos_state   = None  # False: down; True: up
		self.match_state = False # False: non-matched yet

		# define QPushButton properties
		self.setMinimumSize(100,100)
		self.setMaximumSize(150,150)
		self.setDefault(True);
		self.setAutoDefault(False);
		self.clicked.connect(self.toggle_card)

		# make sure card starts face down
		self.toggle_card()

	def toggle_card(self):
		if not self.is_matched():
			if self.is_up() is None or self.is_up() == True:
				icon = self.back_icon
				self.pos_state = False # down
			else:
				icon = self.face_icon
				self.pos_state = True  # up
			self.setIcon(icon)
			self.setIconSize(QtCore.QSize(75,75))

	def is_up(self):
		return self.pos_state 

	def is_matched(self):
		return self.match_state

	def set_matched(self, value):
		self.match_state = value

class Board(QtWidgets.QMainWindow):
	def __init__(self):
		super(Board, self).__init__()
		self.match_counter = 0
		self.click_tracker = deque(maxlen=2)
		self.move_tracker  = deque(maxlen=2)

		self.load_card_icons()
		self.set_card_pairs()
		self.draw_board()

	def load_card_icons(self):
		self.card_type = 'animals'
		if np.random.choice((True,False)):
			self.card_type = 'monsters'
		icon_folder = os.path.join(info.CARDS_DIR, self.card_type)
		filenames = np.random.choice(os.listdir(os.path.join(icon_folder)),
					info.NUM_CARDS, replace=False)
		self.card_icon_paths = []
		for f in filenames:
			self.card_icon_paths.append(os.path.join(icon_folder, f))

	def set_card_pairs(self):
		all_pairs = []
		for i in range(info.BOARD_SIZE):
			for j in range(info.BOARD_SIZE):
				all_pairs.append((i,j))
		np.random.shuffle(all_pairs)
		
		icon_idx = 0
		self.card_pairs = np.empty((info.BOARD_SIZE,info.BOARD_SIZE), dtype=object)
		for i in range(info.BOARD_SIZE):
			for j in range(info.BOARD_SIZE):
				if self.card_pairs[i][j] is None:
					if (i,j) == all_pairs[0]:
						r,c = all_pairs.pop(1)
					else:
						r,c = all_pairs.pop(0)
					self.card_pairs[i][j] = (r, c, icon_idx)
					self.card_pairs[r][c] = (i, j, icon_idx)
					all_pairs.pop(all_pairs.index((i,j)))
					icon_idx += 1

	def draw_board(self):
		question_icon_path = os.path.join(info.CARDS_DIR, 'question.png')
		self.grid = QtWidgets.QGridLayout()
		for i in range(info.BOARD_SIZE):
			for j in range(info.BOARD_SIZE):
				face_icon_path = self.card_icon_paths[self.card_pairs[i][j][2]]
				card = Card(self.card_pairs[i][j][2], face_icon_path, question_icon_path)
				card.clicked.connect(self.check_match)
				self.grid.addWidget(card, i, j)

		# set main ui
		wg_central = QtWidgets.QWidget()
		wg_central.setLayout(self.grid)
		self.setCentralWidget(wg_central)

		# set cursor to the first element at the top-left corner
		self.grid.itemAtPosition(0,0).widget().setFocus()
		self.grid.itemAtPosition(0,0).widget().setStyleSheet(info.HOVER_FOCUS)
		self.move_tracker.append((0, 0, self.card_pairs[0][0][2]))

		# create shortcuts for keyboard arrows
		QtWidgets.QShortcut(QtGui.QKeySequence(QtCore.Qt.Key_Up),    self, self.on_up)
		QtWidgets.QShortcut(QtGui.QKeySequence(QtCore.Qt.Key_Down),  self, self.on_down)
		QtWidgets.QShortcut(QtGui.QKeySequence(QtCore.Qt.Key_Left),  self, self.on_left)
		QtWidgets.QShortcut(QtGui.QKeySequence(QtCore.Qt.Key_Right), self, self.on_right)
		QtWidgets.QShortcut(QtGui.QKeySequence('Ctrl+Q'),            self, self.close)

	def restore_after_unmatch(self, from_click=False):
		if info.DEGUB:
			print('resto', end=' ')
		rows = [mx[0] for mx in self.click_tracker]
		cols = [my[1] for my in self.click_tracker]
		for i in range(2):
			if from_click and (rows[i],cols[i]) == self.move_tracker[-1][:2]:
				continue
			button = self.grid.itemAtPosition(rows[i], cols[i])
			button.widget().toggle_card()
		self.click_tracker.clear()
		if info.DEGUB:
			print(colored(list(self.move_tracker), 'red'), 
						colored(list(self.click_tracker), 'green'))

	def check_match(self):
		if info.DEGUB:
			print('pres1', colored(list(self.move_tracker), 'red'), 
						colored(list(self.click_tracker), 'green'))
		if len(self.click_tracker) == self.click_tracker.maxlen:
			self.restore_after_unmatch(from_click=True)
			return

		self.click_tracker.append(self.move_tracker[-1])
		if len(self.click_tracker) == self.click_tracker.maxlen:
			matches = [midx[2] for midx in self.click_tracker]
			if len(set(matches)) == 1:
				rows = [mx[0] for mx in self.click_tracker]
				cols = [my[1] for my in self.click_tracker]
				if (rows[0],cols[0]) == (rows[1],cols[1]):
					self.click_tracker.clear()
					return
				for i in range(2):
					button = self.grid.itemAtPosition(rows[i], cols[i])
					button.widget().set_matched(True)
				self.match_counter += 1
				if self.match_counter == info.NUM_CARDS:
					self.win()
		if info.DEGUB:
			print('pres2', colored(list(self.move_tracker), 'red'), 
						colored(list(self.click_tracker), 'green'))

	def win(self):
		reply = QtWidgets.QMessageBox.information(self, 
					u'You win', info.WIN_MSG, QtWidgets.QMessageBox.Ok)
		self.close()

	def on_up(self):
		if info.DEGUB:
			print('   up', end=' ')
		self.move_focus(0, -1)

	def on_down(self):
		if info.DEGUB:
			print(' down', end=' ')
		self.move_focus(0, +1)

	def on_left(self):
		if info.DEGUB:
			print(' left', end=' ')
		self.move_focus(-1, 0)

	def on_right(self):
		if info.DEGUB:
			print('right', end=' ')
		self.move_focus(+1, 0)

	def move_focus(self, dx, dy):
		if QtWidgets.qApp.focusWidget() == 0:
			return

		idx = self.grid.indexOf(QtWidgets.qApp.focusWidget())
		if idx == -1:
			return

		r, c, row_span, col_span = self.grid.getItemPosition(idx)
		new_row = r + dy
		new_col = c + dx

		if new_row   > info.BOARD_SIZE-1:
			new_row  = info.BOARD_SIZE-1 # limit the fucking right edge
		elif new_row < 0:
			new_row  = 0                 # limit the fucking left edge
		if new_col   > info.BOARD_SIZE-1:
			new_col  = info.BOARD_SIZE-1 # limit the fucking bottom edge
		elif new_col < 0:
			new_col  = 0                 # limit the fucking top edge

		button = self.grid.itemAtPosition(new_row, new_col)
		if button is None:
			return

		button.widget().setFocus()
		button.widget().setStyleSheet(info.HOVER_FOCUS)
		self.move_tracker.append(
					(new_row, new_col, self.card_pairs[new_row][new_col][2]))
		if info.DEGUB:
			print(colored(list(self.move_tracker), 'red'), 
						colored(list(self.click_tracker), 'green'))
		if len(self.click_tracker) == self.click_tracker.maxlen:
			self.restore_after_unmatch()


if __name__=='__main__':
	app = QtWidgets.QApplication(sys.argv)
	window = Board()
	window.move(300,50)
	window.show()
	sys.exit(app.exec_())
### EOF ###
