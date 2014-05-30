"""

project:		3d-auv-simulator
author:			nishant dania
email: 			nishantdania@gmail.com
modified on:	May 28, 2014

"""

#########################################################################

from ModelNode import ModelNode

class SceneGraphManager(object):
	modelList = []

	def __init__(self,pandaScene):
		self.pandaScene = pandaScene
		self.modelNode = ModelNode(self.pandaScene)

	def addModelNode(self,filename):
		self.filename = filename
		self.modelNode.addModel(self.filename)
		SceneGraphManager.modelList.append(self.modelNode)	

	def setNodeX(self,posX):
		self.posX = float(posX)
		SceneGraphManager.modelList[0].setX(self.posX)

	def setNodeY(self,posY):
		self.posY = float(posY)
		SceneGraphManager.modelList[0].setY(self.posY)

	def setNodeZ(self,posZ):
		self.posZ = float(posZ)
		SceneGraphManager.modelList[0].setZ(self.posZ)

	def setNodeH(self,posH):
		self.posH = float(posH)
		SceneGraphManager.modelList[0].setH(self.posH)

	def setNodeP(self,posP):
		self.posP = float(posP)
		SceneGraphManager.modelList[0].setP(self.posP)

	def setNodeR(self,posR):
		self.posR = float(posR)
		SceneGraphManager.modelList[0].setR(self.posR)

	def setNodeScale(self,scale):
		self.scale = float(scale)
		SceneGraphManager.modelList[0].setScale(self.scale)
