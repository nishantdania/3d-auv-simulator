"""

project:		3d-auv-simulator
author:			nishant dania
email: 			nishantdania@gmail.com
modified on:	June 8, 2014

"""

#########################################################################


from direct.stdpy import threading


class Connections(object):
	def __init__(self, qt, q, em):
		self.queueLock = threading.Lock()
		self.qt = qt
		self.q = q
		self.em = em

		self.connectToAddModel()
		self.connectToSetX()
		self.connectToSetY()
		self.connectToSetZ()
		self.connectToSetH()
		self.connectToSetP()
		self.connectToSetR()
		self.connectToSetScale()
		self.connectToLoadScene()


	""" Functions to add model """

	def connectToAddModel(self):
		self.qt.addModel.connect(lambda: self.dataAddModel(self.qt))
		self.qt.sendAddModel.connect(self.emAddModel)

	def emAddModel(self):
		self.em.messengerAddModel(self.q.get())

	def dataAddModel(self,qt):
		self.modelName = self.qt.getModelName()
		self.queueLock.acquire()
		self.q.put(self.modelName)
		self.queueLock.release()

	""" Functions to setX """

	def connectToSetX(self):
		self.qt.setXEmit.connect(lambda: self.dataSetX(self.qt))
		self.qt.sendSetXEmit.connect(self.emSetX)

	def emSetX(self):
		self.em.messengerSetX(self.q.get())

	def dataSetX(self,qt):
		self.posX = self.qt.getPosX()
		self.queueLock.acquire()
		self.q.put(self.posX)
		self.queueLock.release()

	""" Functions to setX """

	def connectToSetX(self):
		self.qt.setXEmit.connect(lambda: self.dataSetX(self.qt))
		self.qt.sendSetXEmit.connect(self.emSetX)

	def emSetX(self):
		self.em.messengerSetX(self.q.get())

	def dataSetX(self,qt):
		self.posX = self.qt.getPosX()
		self.queueLock.acquire()
		self.q.put(self.posX)
		self.queueLock.release()

	""" Functions to setX """

	def connectToSetX(self):
		self.qt.setXEmit.connect(lambda: self.dataSetX(self.qt))
		self.qt.sendSetXEmit.connect(self.emSetX)

	def emSetX(self):
		self.em.messengerSetX(self.q.get())

	def dataSetX(self,qt):
		self.posX = self.qt.getPosX()
		self.queueLock.acquire()
		self.q.put(self.posX)
		self.queueLock.release()

	""" Functions to setY """

	def connectToSetY(self):
		self.qt.setYEmit.connect(lambda: self.dataSetY(self.qt))
		self.qt.sendSetYEmit.connect(self.emSetY)

	def emSetY(self):
		self.em.messengerSetY(self.q.get())

	def dataSetY(self,qt):
		self.posY = self.qt.getPosY()
		self.queueLock.acquire()
		self.q.put(self.posY)
		self.queueLock.release()

	""" Functions to setZ """

	def connectToSetZ(self):
		self.qt.setZEmit.connect(lambda: self.dataSetZ(self.qt))
		self.qt.sendSetZEmit.connect(self.emSetZ)

	def emSetZ(self):
		self.em.messengerSetZ(self.q.get())

	def dataSetZ(self,qt):
		self.posZ = self.qt.getPosZ()
		self.queueLock.acquire()
		self.q.put(self.posZ)
		self.queueLock.release()

	""" Functions to setH """

	def connectToSetH(self):
		self.qt.setHEmit.connect(lambda: self.dataSetH(self.qt))
		self.qt.sendSetHEmit.connect(self.emSetH)

	def emSetH(self):
		self.em.messengerSetH(self.q.get())

	def dataSetH(self,qt):
		self.posH = self.qt.getPosH()
		self.queueLock.acquire()
		self.q.put(self.posH)
		self.queueLock.release()

	""" Functions to setP """

	def connectToSetP(self):
		self.qt.setPEmit.connect(lambda: self.dataSetP(self.qt))
		self.qt.sendSetPEmit.connect(self.emSetP)

	def emSetP(self):
		self.em.messengerSetP(self.q.get())

	def dataSetP(self,qt):
		self.posP = self.qt.getPosP()
		self.queueLock.acquire()
		self.q.put(self.posP)
		self.queueLock.release()

	""" Functions to setR """

	def connectToSetR(self):
		self.qt.setREmit.connect(lambda: self.dataSetR(self.qt))
		self.qt.sendSetREmit.connect(self.emSetR)

	def emSetR(self):
		self.em.messengerSetR(self.q.get())

	def dataSetR(self,qt):
		self.posR = self.qt.getPosR()
		self.queueLock.acquire()
		self.q.put(self.posR)
		self.queueLock.release()

	""" Functions to setScale """

	def connectToSetScale(self):
		self.qt.setScaleEmit.connect(lambda: self.dataSetScale(self.qt))
		self.qt.sendSetScaleEmit.connect(self.emSetScale)

	def emSetScale(self):
		self.em.messengerSetScale(self.q.get())

	def dataSetScale(self,qt):
		self.scale = self.qt.getScale()
		self.queueLock.acquire()
		self.q.put(self.scale)
		self.queueLock.release()

	""" Functions to Load Scene """

	def connectToLoadScene(self):
		self.qt.loadSceneEmit.connect(lambda: self.dataLoadScene(self.qt))
		self.qt.sendLoadSceneEmit.connect(self.emLoadScene)

	def emLoadScene(self):
		self.em.messengerLoadScene(self.q.get())

	def dataLoadScene(self,qt):
		self.filename = self.qt.getSavedFile()
		self.queueLock.acquire()
		self.q.put(self.filename)
		self.queueLock.release()