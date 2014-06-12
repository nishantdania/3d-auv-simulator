"""

project:		3d-auv-simulator
author:			nishant dania
email: 			nishantdania@gmail.com
modified on:	June 12, 2014

"""

#########################################################################

from panda3d.core import Vec3,Vec4,Point3
from panda3d.core import CollisionRay,CollisionNode,GeomNode,CollisionTraverser
from panda3d.core import CollisionHandlerQueue, CollisionSphere, BitMask32

class MouseHandler(object):
	def __init__(self,pandaScene):
		self.pandaScene = pandaScene

	def setupMouseCollisionWM(self):
		self.mouseTraverser = CollisionTraverser()
		self.mouseCollisionQueue    = CollisionHandlerQueue()
		self.mouseRay = CollisionRay()
		self.mouseRay.setOrigin(self.pandaScene.worldMapCam.getPos(self.pandaScene.render))
		self.mouseRay.setDirection(self.pandaScene.render.getRelativeVector(self.pandaScene.worldMapCam, Vec3(0,1,0)))
		self.mouseNode = CollisionNode('mouseRay')
		self.mouseNode.addSolid(self.mouseRay)
		self.mouseNodePath = self.pandaScene.worldMapCam.attachNewNode(self.mouseNode)
		self.mouseNode.setFromCollideMask(GeomNode.getDefaultCollideMask())
		self.mouseTraverser.addCollider(self.mouseNodePath, self.mouseCollisionQueue)

		# uncomment to see the collisions
		# self.mouseTraverser.showCollisions(self.pandaScene.render)	


	def selectedObjectIdWM(self):
		if (self.pandaScene.worldMapMouse.hasMouse() == False):
			return 0,None
		mpos = self.pandaScene.worldMapMouse.getMouse()
		self.mouseRay.setFromLens(self.pandaScene.camNode, mpos.getX(), mpos.getY())
		self.mouseTraverser.traverse(self.pandaScene.render)

		if (self.mouseCollisionQueue.getNumEntries() > 0):
			self.mouseCollisionQueue.sortEntries()
			entry     = self.mouseCollisionQueue.getEntry(0);
			selectedObj = entry.getIntoNodePath()
			selectedObj = selectedObj.findNetTag('selectable')
			if not selectedObj.isEmpty():
				return selectedObj.getTag('id'),selectedObj
			else:
				return 0,None
		return 0,None

	def selectedObjectId(self):
		if (self.pandaScene.mouseWatcherNode.hasMouse() == False):
			return 0,None
		mpos = base.mouseWatcherNode.getMouse()
		self.mouseRay.setFromLens(self.pandaScene.camNode, mpos.getX(), mpos.getY())
		self.mouseTraverser.traverse(self.pandaScene.render)

		if (self.mouseCollisionQueue.getNumEntries() > 0):
			self.mouseCollisionQueue.sortEntries()
			entry     = self.mouseCollisionQueue.getEntry(0);
			selectedObj = entry.getIntoNodePath()
			selectedObj = selectedObj.findNetTag('selectable')
			if not selectedObj.isEmpty():
				return selectedObj.getTag('id'),selectedObj
			else:
				return 0,None	
		return 0,None

	def setupMouseCollision(self):
		self.mouseTraverser = CollisionTraverser()
		self.mouseCollisionQueue    = CollisionHandlerQueue()
		self.mouseRay = CollisionRay()
		self.mouseRay.setOrigin(self.pandaScene.camera.getPos(self.pandaScene.render))
		self.mouseRay.setDirection(self.pandaScene.render.getRelativeVector(self.pandaScene.camera, Vec3(0,1,0)))
		self.mouseNode = CollisionNode('mouseRay')
		self.mouseNode.addSolid(self.mouseRay)
		self.mouseNodePath = self.pandaScene.camera.attachNewNode(self.mouseNode)
		self.mouseNode.setFromCollideMask(GeomNode.getDefaultCollideMask())
		self.mouseTraverser.addCollider(self.mouseNodePath, self.mouseCollisionQueue)

		# uncomment to see the collisions
		# self.mouseTraverser.showCollisions(self.pandaScene.render)	
