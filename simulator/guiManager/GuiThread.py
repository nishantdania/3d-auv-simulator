"""

project:		3d-auv-simulator
author:			nishant dania
email: 			nishantdania@gmail.com
modified on:	May 26, 2014

"""

#########################################################################


from guiManager import Gui
from direct.stdpy import threading
from PyQt4 import QtGui, QtCore
import sys
from guiManager import Connections

class GuiThread(threading.Thread):
	def __init__(self,q,em):
		threading.Thread.__init__(self)
		self.q = q
		self.em = em

	def run(self):
		app = QtGui.QApplication(sys.argv)
		self.qt = Gui()
		self.qt.show()
		self.connnections = Connections(self.qt, self.q, self.em)
		app.exec_()