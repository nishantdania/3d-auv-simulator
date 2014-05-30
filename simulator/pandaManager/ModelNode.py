"""

project:		3d-auv-simulator
author:			nishant dania
email: 			nishantdania@gmail.com
modified on:	May 28, 2014

"""

#########################################################################

from direct.showbase.DirectObject import DirectObject
from pandac.PandaModules import *

class ModelNode(DirectObject):
	def __init__(self,pandaScene):
		self.pandaScene = pandaScene

	def getfilename(self):
		return self.model.filename

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
		return self.model.getScale()

	def setfilename(self,filename):
		self.model.fileName = filename

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
		self.model.setScale(scale)

	def addModel(self,modelName):
		self.modelName = str(modelName)
		self.pandaFile = Filename.fromOsSpecific(self.modelName)
		self.model = loader.loadModel(self.pandaFile)
		self.model.reparentTo(self.pandaScene.getMainNode())
		self.model.setPos(-8,42,0)
		print "Model Added"