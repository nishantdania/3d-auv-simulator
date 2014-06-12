"""

project:		3d-auv-simulator
author:			nishant dania
email: 			nishantdania@gmail.com
modified on:	June 12, 2014

"""

#########################################################################

from direct.showbase.DirectObject import DirectObject
from pandac.PandaModules import *

class ModelNode(DirectObject):
	def __init__(self,pandaScene):
		self.pandaScene = pandaScene
		self.scale = 1

	def getFilename(self):
		return str(self.filename)

	def getX(self):
		return self.model.getX()

	def getY(self):
		return self.model.getY()

	def getZ(self):
		return self.model.getZ()

	def getH(self):
		return self.model.getH()

	def getP(self):
		return self.model.getP()

	def getR(self):
		return self.model.getR()

	def getScale(self):
		return self.scale

	def setFilename(self,filename):
		self.filename = str(filename)
		self.pandaFile = Filename.fromOsSpecific(self.filename)
		self.filename = filename

	def setX(self,x):
		self.model.setX(x)

	def setY(self,y):
		self.model.setY(y)

	def setZ(self,z):
		self.model.setZ(z)

	def setH(self,h):
		self.model.setH(h)

	def setP(self,p):
		self.model.setP(p)

	def setR(self,r):
		self.model.setR(r)

	def setScale(self,scale):
		self.scale = scale
		self.model.setScale(self.scale)

	def addModel(self,modelName,modelNumber):
		self.modelName = str(modelName)
		self.pandaFile = Filename.fromOsSpecific(self.modelName)
		self.model = loader.loadModel(self.pandaFile)
		self.model.reparentTo(self.pandaScene.getMainNode())
		self.model.setPos(0,0,0)
		self.id = str(modelNumber)
		self.model.setTag("id",self.id)
		self.model.setTag("selectable","1")
		print "Model Added Successfully with id = ",self.model.getTag("id")