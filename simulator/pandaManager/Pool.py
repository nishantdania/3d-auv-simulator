"""

project:		3d-auv-simulator
author:			nishant dania
email: 			nishantdania@gmail.com
modified on:	June 29, 2014

"""

#########################################################################

from pandac.PandaModules import *
from panda3d.core import *
from direct.task import Task

GRID_SIZE = 64
X_SEPARATION = 1
Y_SEPARATION = 1
Z_SEPARATION = 0.5

class Pool(object):

	def __init__(self, pandaScene):

		self.pandaScene = pandaScene

		# create vertices for water plane
		gridPlane = GeomVertexData('grid',GeomVertexFormat.getV3c4t2(),Geom.UHDynamic)
		gridPlane.setNumRows((GRID_SIZE+1)*(GRID_SIZE+1))
		vertex = GeomVertexWriter(gridPlane, 'vertex')
		color = GeomVertexWriter(gridPlane, 'color')
		texcoord = GeomVertexWriter(gridPlane, 'texcoord')

		for y in xrange(0,GRID_SIZE+1):
			for x in xrange(0,GRID_SIZE+1):
				vertex.addData3f((x-GRID_SIZE/2.0)*X_SEPARATION, (y-GRID_SIZE/2.0)*Y_SEPARATION, 0)
				if x%2==0 and y%2==0:
					texcoord.addData2f(0,0)
				if x%2==0 and y%2!=0:
					texcoord.addData2f(0,1)
				if x%2!=0 and y%2==0:
					texcoord.addData2f(1,0)
				if x%2!=0 and y%2!=0:
					texcoord.addData2f(1,1)

		prim = GeomTriangles(Geom.UHStatic)

		# create indices for drawing vertices using triangle self.pandaScene.primitive
		for x in xrange(0,GRID_SIZE):
			for start in xrange((GRID_SIZE*x)+x+1,(GRID_SIZE*x)+x+1+GRID_SIZE):
				prim.addVertices(start, start+GRID_SIZE, start-1)
				prim.addVertices(start, start+GRID_SIZE+1, start+GRID_SIZE)

		geom = Geom(gridPlane)
		geom.addPrimitive(prim)
		waterNode = GeomNode('waterPlane')
		waterNode.addGeom(geom)
		self.pandaScene.waterNP = self.pandaScene.render.attachNewNode(waterNode)		
		# self.pandaScene.waterNP.setRenderModeWireframe() 
		self.pandaScene.waterNP.setTwoSided(True)
		self.pandaScene.waterNP.setTransparency(TransparencyAttrib.MAlpha)
		self.pandaScene.waterNP.setShader(self.pandaScene.waveShader)

		# create back plane boundary
		gridPlane = GeomVertexData('grid',GeomVertexFormat.getV3c4t2(),Geom.UHDynamic)
		gridPlane.setNumRows(4)
		vertex = GeomVertexWriter(gridPlane, 'vertex')
		color = GeomVertexWriter(gridPlane, 'color')
		texcoord = GeomVertexWriter(gridPlane, 'texcoord')

		for y in xrange(0,GRID_SIZE+1):
			for x in xrange(0,GRID_SIZE+1):
				vertex.addData3f((x-GRID_SIZE/2.0)*X_SEPARATION, GRID_SIZE/2.0*Y_SEPARATION, Z_SEPARATION*((y-GRID_SIZE/2.0)-(GRID_SIZE/2-GRID_SIZE/10)))
				if x%2==0 and y%2==0:
					texcoord.addData2f(0,0)
				if x%2==0 and y%2!=0:
					texcoord.addData2f(0,1)
				if x%2!=0 and y%2==0:
					texcoord.addData2f(1,0)
				if x%2!=0 and y%2!=0:
					texcoord.addData2f(1,1)
		# vertex.addData3f((-GRID_SIZE/2.0)*X_SEPARATION, GRID_SIZE/2.0*Y_SEPARATION, Z_SEPARATION*((-GRID_SIZE/2.0)-(GRID_SIZE/2-GRID_SIZE/10)))
		# vertex.addData3f((GRID_SIZE/2.0)*X_SEPARATION, GRID_SIZE/2.0*Y_SEPARATION, Z_SEPARATION*((-GRID_SIZE/2.0)-(GRID_SIZE/2-GRID_SIZE/10)))
		# vertex.addData3f((-GRID_SIZE/2.0)*X_SEPARATION, GRID_SIZE/2.0*Y_SEPARATION, Z_SEPARATION*((GRID_SIZE/2.0)-(GRID_SIZE/2-GRID_SIZE/10)))
		# vertex.addData3f((GRID_SIZE/2.0)*X_SEPARATION, GRID_SIZE/2.0*Y_SEPARATION, Z_SEPARATION*((GRID_SIZE/2.0)-(GRID_SIZE/2-GRID_SIZE/10)))
		# texcoord.addData2f(0,0)
		# texcoord.addData2f(0,1)
		# texcoord.addData2f(1,0)
		# texcoord.addData2f(1,1)

		# prim = GeomTriangles(Geom.UHStatic)

		# create indices for drawing vertices using triangle primitive
		for x in xrange(0,GRID_SIZE):
			for start in xrange((GRID_SIZE*x)+x+1,(GRID_SIZE*x)+x+1+GRID_SIZE):
				prim.addVertices(start, start+GRID_SIZE, start-1)
				prim.addVertices(start, start+GRID_SIZE+1, start+GRID_SIZE)

		prim.addVertices(0,1,2)
		prim.addVertices(1,3,2)

		geom = Geom(gridPlane)
		geom.addPrimitive(prim)
		poolBorderNode = GeomNode('Pool Border')
		poolBorderNode.addGeom(geom)

		# create front plane boundary
		gridPlane = GeomVertexData('grid',GeomVertexFormat.getV3c4t2(),Geom.UHDynamic)
		gridPlane.setNumRows(4)
		vertex = GeomVertexWriter(gridPlane, 'vertex')
		color = GeomVertexWriter(gridPlane, 'color')
		texcoord = GeomVertexWriter(gridPlane, 'texcoord')

		for y in xrange(0,GRID_SIZE+1):
			for x in xrange(0,GRID_SIZE+1):
				vertex.addData3f((x-GRID_SIZE/2.0)*X_SEPARATION, -GRID_SIZE/2.0*Y_SEPARATION, Z_SEPARATION*((y-GRID_SIZE/2.0)-(GRID_SIZE/2-GRID_SIZE/10)))
				if x%2==0 and y%2==0:
					texcoord.addData2f(0,0)
				if x%2==0 and y%2!=0:
					texcoord.addData2f(0,1)
				if x%2!=0 and y%2==0:
					texcoord.addData2f(1,0)
				if x%2!=0 and y%2!=0:
					texcoord.addData2f(1,1)
		# vertex.addData3f((-GRID_SIZE/2.0)*X_SEPARATION, -GRID_SIZE/2.0*Y_SEPARATION, Z_SEPARATION*((-GRID_SIZE/2.0)-(GRID_SIZE/2-GRID_SIZE/10)))
		# vertex.addData3f((GRID_SIZE/2.0)*X_SEPARATION, -GRID_SIZE/2.0*Y_SEPARATION, Z_SEPARATION*((-GRID_SIZE/2.0)-(GRID_SIZE/2-GRID_SIZE/10)))
		# vertex.addData3f((-GRID_SIZE/2.0)*X_SEPARATION, -GRID_SIZE/2.0*Y_SEPARATION, Z_SEPARATION*((GRID_SIZE/2.0)-(GRID_SIZE/2-GRID_SIZE/10)))
		# vertex.addData3f((GRID_SIZE/2.0)*X_SEPARATION, -GRID_SIZE/2.0*Y_SEPARATION, Z_SEPARATION*((GRID_SIZE/2.0)-(GRID_SIZE/2-GRID_SIZE/10)))
		# texcoord.addData2f(0,0)
		# texcoord.addData2f(0,1)
		# texcoord.addData2f(1,0)
		# texcoord.addData2f(1,1)

		prim = GeomTriangles(Geom.UHStatic)

		# create indices for drawing vertices using triangle primitive
		for x in xrange(0,GRID_SIZE):
			for start in xrange((GRID_SIZE*x)+x+1,(GRID_SIZE*x)+x+1+GRID_SIZE):
				prim.addVertices(start, start-1, start+GRID_SIZE)
				prim.addVertices(start, start+GRID_SIZE, start+GRID_SIZE+1)

		# prim.addVertices(0,2,1)
		# prim.addVertices(1,2,3)

		geom = Geom(gridPlane)
		geom.addPrimitive(prim)
		poolBorderNode.addGeom(geom)

		# create left plane boundary
		gridPlane = GeomVertexData('grid',GeomVertexFormat.getV3c4t2(),Geom.UHDynamic)
		gridPlane.setNumRows((GRID_SIZE+1)*(GRID_SIZE+1))
		vertex = GeomVertexWriter(gridPlane, 'vertex')
		color = GeomVertexWriter(gridPlane, 'color')
		texcoord = GeomVertexWriter(gridPlane, 'texcoord')

		for y in xrange(0,GRID_SIZE+1):
			for x in xrange(0,GRID_SIZE+1):
				vertex.addData3f(X_SEPARATION*(-GRID_SIZE/2.0), (x-GRID_SIZE/2.0)*Y_SEPARATION, Z_SEPARATION*((y-GRID_SIZE/2.0)-(GRID_SIZE/2-GRID_SIZE/10)))
				if x%2==0 and y%2==0:
					texcoord.addData2f(0,0)
				if x%2==0 and y%2!=0:
					texcoord.addData2f(0,1)
				if x%2!=0 and y%2==0:
					texcoord.addData2f(1,0)
				if x%2!=0 and y%2!=0:
					texcoord.addData2f(1,1)

		# vertex.addData3f(X_SEPARATION*(-GRID_SIZE/2.0), (-GRID_SIZE/2.0)*Y_SEPARATION, Z_SEPARATION*((-GRID_SIZE/2.0)-(GRID_SIZE/2-GRID_SIZE/10)))
		# vertex.addData3f(X_SEPARATION*(-GRID_SIZE/2.0), (GRID_SIZE/2.0)*Y_SEPARATION, Z_SEPARATION*((-GRID_SIZE/2.0)-(GRID_SIZE/2-GRID_SIZE/10)))
		# vertex.addData3f(X_SEPARATION*(-GRID_SIZE/2.0), (-GRID_SIZE/2.0)*Y_SEPARATION, Z_SEPARATION*((GRID_SIZE/2.0)-(GRID_SIZE/2-GRID_SIZE/10)))
		# vertex.addData3f(X_SEPARATION*(-GRID_SIZE/2.0), (GRID_SIZE/2.0)*Y_SEPARATION, Z_SEPARATION*((GRID_SIZE/2.0)-(GRID_SIZE/2-GRID_SIZE/10)))
		# texcoord.addData2f(0,0)
		# texcoord.addData2f(0,1)
		# texcoord.addData2f(1,0)
		# texcoord.addData2f(1,1)

		prim = GeomTriangles(Geom.UHStatic)

		# create indices for drawing vertices using triangle primitive
		for x in xrange(0,GRID_SIZE):
			for start in xrange((GRID_SIZE*x)+x+1,(GRID_SIZE*x)+x+1+GRID_SIZE):
				prim.addVertices(start, start+GRID_SIZE, start-1)
				prim.addVertices(start, start+GRID_SIZE+1, start+GRID_SIZE)

		# prim.addVertices(0,1,2)
		# prim.addVertices(1,3,2)

		geom = Geom(gridPlane)
		geom.addPrimitive(prim)
		poolBorderNode.addGeom(geom)

		# create right plane boundary
		gridPlane = GeomVertexData('grid',GeomVertexFormat.getV3c4t2(),Geom.UHDynamic)
		gridPlane.setNumRows((GRID_SIZE+1)*(GRID_SIZE+1))
		vertex = GeomVertexWriter(gridPlane, 'vertex')
		color = GeomVertexWriter(gridPlane, 'color')
		texcoord = GeomVertexWriter(gridPlane, 'texcoord')

		for y in xrange(0,GRID_SIZE+1):
			for x in xrange(0,GRID_SIZE+1):
				vertex.addData3f(X_SEPARATION*GRID_SIZE/2.0, (x-GRID_SIZE/2.0)*Y_SEPARATION, Z_SEPARATION*((y-GRID_SIZE/2.0)-(GRID_SIZE/2-GRID_SIZE/10)))
				if x%2==0 and y%2==0:
					texcoord.addData2f(0,0)
				if x%2==0 and y%2!=0:
					texcoord.addData2f(0,1)
				if x%2!=0 and y%2==0:
					texcoord.addData2f(1,0)
				if x%2!=0 and y%2!=0:
					texcoord.addData2f(1,1)

		# vertex.addData3f(X_SEPARATION*GRID_SIZE/2.0, (-GRID_SIZE/2.0)*Y_SEPARATION, Z_SEPARATION*((-GRID_SIZE/2.0)-(GRID_SIZE/2-GRID_SIZE/10)))
		# vertex.addData3f(X_SEPARATION*GRID_SIZE/2.0, (GRID_SIZE/2.0)*Y_SEPARATION, Z_SEPARATION*((-GRID_SIZE/2.0)-(GRID_SIZE/2-GRID_SIZE/10)))
		# vertex.addData3f(X_SEPARATION*GRID_SIZE/2.0, (-GRID_SIZE/2.0)*Y_SEPARATION, Z_SEPARATION*((GRID_SIZE/2.0)-(GRID_SIZE/2-GRID_SIZE/10)))
		# vertex.addData3f(X_SEPARATION*GRID_SIZE/2.0, (GRID_SIZE/2.0)*Y_SEPARATION, Z_SEPARATION*((GRID_SIZE/2.0)-(GRID_SIZE/2-GRID_SIZE/10)))
		# texcoord.addData2f(0,0)
		# texcoord.addData2f(0,1)
		# texcoord.addData2f(1,0)
		# texcoord.addData2f(1,1)

		prim = GeomTriangles(Geom.UHStatic)

		# create indices for drawing vertices using triangle primitive
		for x in xrange(0,GRID_SIZE):
			for start in xrange((GRID_SIZE*x)+x+1,(GRID_SIZE*x)+x+1+GRID_SIZE):
				prim.addVertices(start, start-1, start+GRID_SIZE)
				prim.addVertices(start, start+GRID_SIZE, start+GRID_SIZE+1)

		# prim.addVertices(0,2,1)
		# prim.addVertices(1,2,3)

		geom = Geom(gridPlane)
		geom.addPrimitive(prim)
		poolBorderNode.addGeom(geom)

		# create bottom plane boundary
		gridPlane = GeomVertexData('grid',GeomVertexFormat.getV3c4t2(),Geom.UHDynamic)
		gridPlane.setNumRows((GRID_SIZE+1)*(GRID_SIZE+1))
		vertex = GeomVertexWriter(gridPlane, 'vertex')
		color = GeomVertexWriter(gridPlane, 'color')
		texcoord = GeomVertexWriter(gridPlane, 'texcoord')

		for y in xrange(0,GRID_SIZE+1):
			for x in xrange(0,GRID_SIZE+1):
				vertex.addData3f((x-GRID_SIZE/2.0)*X_SEPARATION, (y-GRID_SIZE/2.0)*Y_SEPARATION,-(GRID_SIZE-GRID_SIZE/10)*Z_SEPARATION)
				if x%2==0 and y%2==0:
					texcoord.addData2f(0,0)
				if x%2==0 and y%2!=0:
					texcoord.addData2f(0,1)
				if x%2!=0 and y%2==0:
					texcoord.addData2f(1,0)
				if x%2!=0 and y%2!=0:
					texcoord.addData2f(1,1)

		# vertex.addData3f((-GRID_SIZE/2.0)*X_SEPARATION, (-GRID_SIZE/2.0)*Y_SEPARATION, -(GRID_SIZE-GRID_SIZE/10)*Z_SEPARATION)
		# vertex.addData3f((GRID_SIZE/2.0)*X_SEPARATION, (-GRID_SIZE/2.0)*Y_SEPARATION,-(GRID_SIZE-GRID_SIZE/10)*Z_SEPARATION)
		# vertex.addData3f((-GRID_SIZE/2.0)*X_SEPARATION, (GRID_SIZE/2.0)*Y_SEPARATION,-(GRID_SIZE-GRID_SIZE/10)*Z_SEPARATION)
		# vertex.addData3f((GRID_SIZE/2.0)*X_SEPARATION, (GRID_SIZE/2.0)*Y_SEPARATION,-(GRID_SIZE-GRID_SIZE/10)*Z_SEPARATION)
		# texcoord.addData2f(0,0)
		# texcoord.addData2f(0,1)
		# texcoord.addData2f(1,0)
		# texcoord.addData2f(1,1)

		prim = GeomTriangles(Geom.UHStatic)

		# create indices for drawing vertices using triangle self.pandaScene.primitive
		for x in xrange(0,GRID_SIZE):
			for start in xrange((GRID_SIZE*x)+x+1,(GRID_SIZE*x)+x+1+GRID_SIZE):
				prim.addVertices(start, start+GRID_SIZE, start-1)
				prim.addVertices(start, start+GRID_SIZE+1, start+GRID_SIZE)

		# prim.addVertices(0,1,2)
		# prim.addVertices(1,3,2)


		geom = Geom(gridPlane)
		geom.addPrimitive(prim)
		poolBorderNode.addGeom(geom)


		# load tile texture
		texture = loader.loadTexture("poolTex.jpg")
		texture.setWrapU(Texture.WMClamp)
		texture.setWrapV(Texture.WMClamp)

		# add shader to underwater planes
		self.pandaScene.poolBorder = self.pandaScene.render.attachNewNode(poolBorderNode)		
		# self.pandaScene.poolBorder.setRenderModeWireframe() 
		self.pandaScene.poolBorder.reparentTo(self.pandaScene.UWNode)
		self.pandaScene.UWNode.setShader(self.pandaScene.UWShader)
		self.pandaScene.UWNode.setShaderInput("camPos",base.camera.getX() ,base.camera.getY() ,base.camera.getZ() ,1.0)
		taskMgr.add(self.updateShader, 'updateShader')
		ts = TextureStage('ts')
		self.pandaScene.UWNode.setTexture(ts,texture)


	def updateShader(self,task):
		self.pandaScene.UWNode.setShaderInput("camPos",base.camera.getX() ,base.camera.getY() ,base.camera.getZ() ,1.0)
		return task.cont
