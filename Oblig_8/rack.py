class Rack:
	## oppretter et rack der det senere kan plasseres noder
	#
	def __init__(self,maxnodes):
		self._maxnodes = maxnodes
		self._nodes = []
	## Plasserer en ny node inn i racket
	#  @param node noden som skal plasseres inn
	def settInn(self, node):
		self._nodes.append(node)

	## Henter antall noder i racket
	# @return antall noder
	def getAntNoder(self):
		return len(self._nodes)

	## Beregner sammenlagt antall prosessorer i nodene i et rack
	# @return antall prosessorer
	def antProsessorer(self):
		counter = 0
		for node in self._nodes:
			counter += node.antProsessorer()
		return counter

	## Beregner antall noder i racket med minne over gitt grense
	# @param paakrevdMinne antall GB minne som kreves
	# @return antall noder med tilstrekkelig minne
	def noderMedNokMinne(self, paakrevdMinne):
		counter = 0
		for node in self._nodes:
			if node.nokMinne(paakrevdMinne):
				counter += 1
		return counter
