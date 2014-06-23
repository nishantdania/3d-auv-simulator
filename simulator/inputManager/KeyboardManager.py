"""

project:		3d-auv-simulator
author:			nishant dania
email: 			nishantdania@gmail.com
modified on:	June 12, 2014

"""

#########################################################################


from direct.showbase import DirectObject
import sys
from MouseHandler import MouseHandler
from utils import Globals

class KeyboardManager(DirectObject.DirectObject):
	def __init__(self,panda):
		self.pandaScene = panda
		self.worldMapEnabled = False
		self.selectionEnabled = False
		self.currentSelection = None
		self.previousSelection = None
		self.accept("escape", self.pressedEscape)
		self.accept("r", self.pressedR)
		self.accept("o", self.pressedO)
		self.accept("m", self.pressedM)
		self.accept("z",self.pressedZ)
		self.accept("x",self.pressedX)
		self.accept("c",self.pressedC)
		self.accept("w",self.pressedW)
		self.accept("a",self.pressedA)
		self.accept("s",self.pressedS)
		self.accept("d",self.pressedD)
		self.accept("1",self.pressed1)
		self.accept("mouse1", self.pressedM1)

	def pressedEscape(self):
		print "exiting..."
		sys.exit(0)

	def pressedR(self):
		print "resetting scene..."
		self.resetScene()

	def pressedO(self):
		print "oobe toggled"
		self.pandaScene.oobe()

	def pressedM(self):
		if not self.worldMapEnabled:
			self.pandaScene.showWorldMap()
			self.worldMapEnabled = True

		else:
			self.worldMapEnabled = False
			self.pandaScene.hideWorldMap()
			

	def pressedZ(self):
		if self.worldMapEnabled:
			self.pandaScene.worldMapCam.setZ(self.pandaScene.worldMapCam.getZ() + self.pandaScene.worldMapCam.getZ()/10)

	def pressedX(self):
		if self.worldMapEnabled:
			self.pandaScene.worldMapCam.setZ(self.pandaScene.worldMapCam.getZ() - self.pandaScene.worldMapCam.getZ()/10)

	def pressedC(self):
		if self.worldMapEnabled:
			self.pandaScene.worldMapCam.setZ(50)
			self.pandaScene.worldMapCam.setX(0)
			self.pandaScene.worldMapCam.setY(0)

	def pressedW(self):
		if self.worldMapEnabled:
			self.pandaScene.worldMapCam.setY(self.pandaScene.worldMapCam.getY() + self.pandaScene.worldMapCam.getZ()/20)

	def pressedA(self):
		if self.worldMapEnabled:
			self.pandaScene.worldMapCam.setX(self.pandaScene.worldMapCam.getX() - self.pandaScene.worldMapCam.getZ()/20)

	def pressedS(self):
		if self.worldMapEnabled:
			self.pandaScene.worldMapCam.setY(self.pandaScene.worldMapCam.getY() - self.pandaScene.worldMapCam.getZ()/20)

	def pressedD(self):
		if self.worldMapEnabled:
			self.pandaScene.worldMapCam.setX(self.pandaScene.worldMapCam.getX() + self.pandaScene.worldMapCam.getZ()/20)

	def pressed1(self):
		if self.selectionEnabled:
			print "Selection Mode Off"
			base.enableMouse()
			self.selectionEnabled = False
		else:
			print "Selection Mode On"
			base.disableMouse()
			self.selectionEnabled = True

	def pressedM1(self):
		if self.selectionEnabled:
			self.mouseHandler = MouseHandler(self.pandaScene)
			self.mouseHandler.setupMouseCollision()
			self.selectedObjectId,self.currentSelection = self.mouseHandler.selectedObjectId()
			if self.currentSelection != None:
				if self.previousSelection != None:
					self.previousSelection.reparentTo(self.pandaScene.mainNode)
				self.currentSelection.reparentTo(self.pandaScene.selectedNode)
				self.previousSelection = self.currentSelection
				Globals.prevSelection = Globals.selection
				Globals.selection = int(self.selectedObjectId)

			if self.worldMapEnabled:
				if(self.pandaScene.worldMapMouse.hasMouse()):
					mpos = self.pandaScene.worldMapMouse.getMouse()
					self.mouseHandler = MouseHandler(self.pandaScene)
					self.mouseHandler.setupMouseCollisionWM()
					self.selectedObjectId,self.currentSelection = self.mouseHandler.selectedObjectIdWM()
					if self.currentSelection != None:
						if self.previousSelection != None:
							self.previousSelection.reparentTo(self.pandaScene.mainNode)
						self.currentSelection.reparentTo(self.pandaScene.selectedNode)
						self.previousSelection = self.currentSelection
						Globals.prevSelection = Globals.selection
						Globals.selection = int(self.selectedObjectId)

	def resetScene(self):
		Globals.modelList = []
		Globals.count = -1
		Globals.selection = -1
		Globals.PrevSelection = -1
		self.pandaScene.mainNode.removeNode()
		self.pandaScene.selectedNode.removeNode()
		if self.worldMapEnabled:
			self.pandaScene.hideWorldMap()
			self.worldMapEnabled = False
		self.pandaScene.mainNode = render.attachNewNode("Main Node")
		self.pandaScene.selectedNode = render.attachNewNode("Selected Node")
		self.pandaScene.selectedNode.showTightBounds()