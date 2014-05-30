"""

project:		3d-auv-simulator
author:			nishant dania
email: 			nishantdania@gmail.com
modified on:	May 28, 2014

"""

#########################################################################


from direct.showbase import DirectObject
import sys

class KeyboardManager(DirectObject.DirectObject):
	def __init__(self,panda):
		self.pandaScene = panda
		self.accept("escape", self.pressedEscape)
		self.accept("r", self.pressedR)
		self.accept("o", self.pressedO)

	def pressedEscape(self):
		print "exiting..."
		sys.exit(0)

	def pressedR(self):
		print "resetting scene..."
		self.resetScene()

	def pressedO(self):
		print "oobe toggled"
		self.pandaScene.oobe()

	def resetScene(self):
		self.pandaScene.model.removeNode()
		self.pandaScene.dummyNode = render.attachNewNode("Dummy Node")
		self.pandaScene.model = self.pandaScene.loader.loadModel("models/environment")
		self.pandaScene.model.reparentTo(self.pandaScene.dummyNode)
		self.pandaScene.model.setScale(0.25,0.25,0.25)
		self.pandaScene.model.setPos(-8,42,0)
		
		
