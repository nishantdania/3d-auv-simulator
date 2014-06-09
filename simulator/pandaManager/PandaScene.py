"""

project:		3d-auv-simulator
author:			nishant dania
email: 			nishantdania@gmail.com
modified on:	June 8, 2014

"""

#########################################################################


from direct.showbase.ShowBase import ShowBase
from pandac.PandaModules import WindowProperties
from pandac.PandaModules import loadPrcFileData
from panda3d.core import Filename
from inputManager import KeyboardManager

# loadPrcFileData("", "undecorated 1")
loadPrcFileData("","window-title 3D AUV Simulator")

class PandaScene(ShowBase):
	def __init__(self):
		self.countModels = 0
		ShowBase.__init__(self)
		base.useDrive()
		wp = WindowProperties.getDefault()
		wp.setOrigin(0,0)
		base.win.requestProperties(wp)
		self.mainNode = render.attachNewNode("Main Node")
		self.initScene()
		self.pandaKeys = KeyboardManager(self)
		
	def initScene(self):
		self.model = self.loader.loadModel("models/environment")
		self.model.reparentTo(self.mainNode)
		self.model.setScale(0.25,0.25,0.25)
		self.model.setPos(-8,42,0)
		print "Simulator Initialized"

	def getMainNode(self):
		return self.mainNode
