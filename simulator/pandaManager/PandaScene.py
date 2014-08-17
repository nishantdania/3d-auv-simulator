"""

project:		3d-auv-simulator
author:			nishant dania
email: 			nishantdania@gmail.com
modified on:	June 29, 2014

"""

#########################################################################


from direct.showbase.ShowBase import ShowBase
from pandac.PandaModules import *
from pandac.PandaModules import loadPrcFileData
from panda3d.core import Filename
from inputManager import KeyboardManager
from Pool import Pool
from rosManager import RosManager

# loadPrcFileData("", "undecorated 1")
loadPrcFileData("","window-title 3D AUV Simulator")

class PandaScene(ShowBase):
	def __init__(self):
		ShowBase.__init__(self)
		# base.useDrive()
		# TODO: Mouse Control
		# base.disableMouse()
		wp = WindowProperties.getDefault()
		wp.setOrigin(0,0)
		base.win.requestProperties(wp)
		self.waveShader = loader.loadShader("wave.sha")
		self.UWShader = loader.loadShader("underwater.sha")
		self.UWMShader = loader.loadShader("UWModel.sha")
		self.mainNode = render.attachNewNode("Main Node")
		self.selectedNode = render.attachNewNode("Selected")
		self.selectedNode.showTightBounds()
		self.UWNode = render.attachNewNode("Underwater Node")
		self.initScene()
		self.pandaKeys = KeyboardManager(self)
		base.setBackgroundColor(1.0, 1.0, 1.0)
		
	def initScene(self):
		self.pool = Pool(self)
		# plight = PointLight('plight')
		# plight.setColor(VBase4(0.0, 0.8, 0.8, 1))
		# plnp = render.attachNewNode(plight)
		# plnp.setPos(0, 3, 1)
		# render.setLight(plnp)
		# self.model = self.loader.loadModel("panda")
		# self.model.reparentTo(self.mainNode)
		# # self.model.setScale(0.25,0.25,0.25)
		# self.model.setPos(-8,42,0)
		# self.camera.setPosHpr(0,0,2,0,0,0)
		# base.enableMouse()
		print "Simulator Initialized"
		RosManager()

	def getMainNode(self):
		return self.mainNode

	def showWorldMap(self):
		self.worldMap = base.win.makeDisplayRegion(0.7, 1, 0, 0.3)
		self.worldMap.setClearColor(VBase4(0.8, 0.8, 0.8, 1))
		self.worldMap.setClearColorActive(True)
		self.worldMap.setClearDepthActive(True)
		self.worldMapCam = self.mainNode.attachNewNode(Camera('worldMapCam'))
		self.worldMap.setCamera(self.worldMapCam)
		self.worldMapCam.setPosHpr(0, 0, 200,0,-90,0)
		self.worldMapCam.node().getLens().setAspectRatio(float(self.worldMap.getPixelWidth()) / float(self.worldMap.getPixelHeight()))
		self.worldMapMouse = MouseWatcher('World Map Mouse')
		self.worldMapMouseNode = base.mouseWatcher.getParent().attachNewNode(self.worldMapMouse)
		self.worldMapMouse.setDisplayRegion(self.worldMap) 

	def hideWorldMap(self):
		self.worldMapMouseNode.removeNode()
		base.win.removeDisplayRegion(self.worldMap)
		self.worldMapCam.removeNode()
