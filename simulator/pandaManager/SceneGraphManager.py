"""

project:		3d-auv-simulator
author:			nishant dania
email: 			nishantdania@gmail.com
modified on:	June 12, 2014

"""

#########################################################################

from ModelNode import ModelNode
from optionManager import LoadScene
from utils import Globals

class SceneGraphManager(object):

	def __init__(self,pandaScene):
		self.pandaScene = pandaScene

	def addModelNode(self,filename):
		Globals.count = Globals.count+1
		Globals.selection = Globals.count
		self.filename = filename
		Globals.modelList.append(ModelNode(self.pandaScene))
		Globals.modelList[Globals.count].addModel(self.filename,Globals.count)
		Globals.modelList[Globals.count].setFilename(self.filename)		

	def setNodeX(self,posX):
		self.posX = float(posX)
		Globals.modelList[Globals.selection].setX(self.posX)

	def setNodeY(self,posY):
		self.posY = float(posY)
		Globals.modelList[Globals.selection].setY(self.posY)

	def setNodeZ(self,posZ):
		self.posZ = float(posZ)
		Globals.modelList[Globals.selection].setZ(self.posZ)

	def setNodeH(self,posH):
		self.posH = float(posH)
		Globals.modelList[Globals.selection].setH(self.posH)

	def setNodeP(self,posP):
		self.posP = float(posP)
		Globals.modelList[Globals.selection].setP(self.posP)

	def setNodeR(self,posR):
		self.posR = float(posR)
		Globals.modelList[Globals.selection].setR(self.posR)

	def setNodeScale(self,scale):
		self.scale = float(scale)
		Globals.modelList[Globals.selection].setScale(self.scale)

	def loadScene(self,filename):
		self.loadFilename = str(filename)
		loadScene = LoadScene(self.loadFilename,self)