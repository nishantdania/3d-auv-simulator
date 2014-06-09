"""

project:		3d-auv-simulator
author:			nishant dania
email: 			nishantdania@gmail.com
modified on:	June 8, 2014

"""

#########################################################################

from ModelNode import ModelNode
from optionManager import LoadScene

class SceneGraphManager(object):
	modelList = []
	count = -1

	def __init__(self,pandaScene):
		self.pandaScene = pandaScene

	def addModelNode(self,filename):
		SceneGraphManager.count = SceneGraphManager.count+1
		self.filename = filename
		SceneGraphManager.modelList.append(ModelNode(self.pandaScene))
		SceneGraphManager.modelList[SceneGraphManager.count].addModel(self.filename)
		SceneGraphManager.modelList[SceneGraphManager.count].setFilename(self.filename)
		

	def setNodeX(self,posX):
		self.posX = float(posX)
		SceneGraphManager.modelList[SceneGraphManager.count].setX(self.posX)

	def setNodeY(self,posY):
		self.posY = float(posY)
		SceneGraphManager.modelList[SceneGraphManager.count].setY(self.posY)

	def setNodeZ(self,posZ):
		self.posZ = float(posZ)
		SceneGraphManager.modelList[SceneGraphManager.count].setZ(self.posZ)

	def setNodeH(self,posH):
		self.posH = float(posH)
		SceneGraphManager.modelList[SceneGraphManager.count].setH(self.posH)

	def setNodeP(self,posP):
		self.posP = float(posP)
		SceneGraphManager.modelList[SceneGraphManager.count].setP(self.posP)

	def setNodeR(self,posR):
		self.posR = float(posR)
		SceneGraphManager.modelList[SceneGraphManager.count].setR(self.posR)

	def setNodeScale(self,scale):
		self.scale = float(scale)
		SceneGraphManager.modelList[SceneGraphManager.count].setScale(self.scale)

	def loadScene(self,filename):
		self.loadFilename = str(filename)
		loadScene = LoadScene(self.loadFilename,self)