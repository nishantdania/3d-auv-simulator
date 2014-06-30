"""

project:		3d-auv-simulator
author:			nishant dania
email: 			nishantdania@gmail.com
modified on:	June 29, 2014

"""

#########################################################################

import sys
from pandac.PandaModules import *
from panda3d.core import *
from direct.task import Task

GRID_SIZE = 64
X_SEPARATION = 2
Y_SEPARATION = 2

class Grid(object):
	def __init__(self, pandaScene):

		self.pandaScene = pandaScene

		# create vertices for water plane
		self.pandaScene.gridPlane = GeomVertexData('grid',GeomVertexFormat.getV3c4(),Geom.UHDynamic)
		self.pandaScene.gridPlane.setNumRows((GRID_SIZE+1)*(GRID_SIZE+1))
		self.pandaScene.vertex = GeomVertexWriter(self.pandaScene.gridPlane, 'vertex')
		self.pandaScene.color = GeomVertexWriter(self.pandaScene.gridPlane, 'color')

		for y in xrange(0,GRID_SIZE+1):
			for x in xrange(0,GRID_SIZE+1):
				self.pandaScene.vertex.addData3f((x-GRID_SIZE/2.0)*X_SEPARATION, (y-GRID_SIZE/2.0)*Y_SEPARATION, 0)

		self.pandaScene.prim = GeomTriangles(Geom.UHStatic)

		# create indices for drawing vertices using triangle self.pandaScene.primitive
		for x in xrange(0,GRID_SIZE):
			for start in xrange((GRID_SIZE*x)+x+1,(GRID_SIZE*x)+x+1+GRID_SIZE):
				self.pandaScene.prim.addVertices(start, start+GRID_SIZE, start-1)
				self.pandaScene.prim.addVertices(start, start+GRID_SIZE+1, start+GRID_SIZE)


		geom = Geom(self.pandaScene.gridPlane)
		geom.addPrimitive(self.pandaScene.prim)
		node = GeomNode('gnode')
		node.addGeom(geom)
		 
		self.pandaScene.waterNP = self.pandaScene.render.attachNewNode(node)
		# self.pandaScene.waterNP.setRenderModeWireframe() 