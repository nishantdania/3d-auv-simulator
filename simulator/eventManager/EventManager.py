"""

project:		3d-auv-simulator
author:			nishant dania
email: 			nishantdania@gmail.com
modified on:	May 28, 2014

"""

#########################################################################


from direct.showbase import DirectObject

class EventManager(DirectObject.DirectObject):
	def __init__(self,pandaScene):
		self.pandaScene = pandaScene

		self.accept('addModel',self.pandaAddModel)
		self.accept('setX',self.pandaSetX)
		self.accept('setY',self.pandaSetY)
		self.accept('setZ',self.pandaSetZ)
		self.accept('setH',self.pandaSetH)
		self.accept('setP',self.pandaSetP)
		self.accept('setR',self.pandaSetR)
		self.accept('setScale',self.pandaSetScale)

		
		""" Functions to add model """

	def pandaAddModel(self):
		self.pandaScene.sceneGraphManager.addModelNode(self.modelName)

	def messengerAddModel(self,modelName):
		self.modelName = modelName
		messenger.send('addModel')


		""" Functions to setX """

	def pandaSetX(self):
		self.pandaScene.sceneGraphManager.setNodeX(self.posX)

	def messengerSetX(self,posX):
		self.posX = posX
		messenger.send('setX')

		""" Functions to setY """

	def pandaSetY(self):
		self.pandaScene.sceneGraphManager.setNodeY(self.posY)

	def messengerSetY(self,posY):
		self.posY = posY
		messenger.send('setY')

		""" Functions to setZ """

	def pandaSetZ(self):
		self.pandaScene.sceneGraphManager.setNodeZ(self.posZ)

	def messengerSetZ(self,posZ):
		self.posZ = posZ
		messenger.send('setZ')

		""" Functions to setH """

	def pandaSetH(self):
		self.pandaScene.sceneGraphManager.setNodeH(self.posH)

	def messengerSetH(self,posH):
		self.posH = posH
		messenger.send('setH')

		""" Functions to setP """

	def pandaSetP(self):
		self.pandaScene.sceneGraphManager.setNodeP(self.posP)

	def messengerSetP(self,posP):
		self.posP = posP
		messenger.send('setP')

		""" Functions to setR """

	def pandaSetR(self):
		self.pandaScene.sceneGraphManager.setNodeR(self.posR)

	def messengerSetR(self,posR):
		self.posR = posR
		messenger.send('setR')

		""" Functions to setScale """

	def pandaSetScale(self):
		self.pandaScene.sceneGraphManager.setNodeScale(self.scale)

	def messengerSetScale(self,scale):
		self.scale = scale
		messenger.send('setScale')