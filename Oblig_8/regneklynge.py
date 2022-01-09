from rack import Rack

class Regneklynge:
	## Oppretter tom regneklynge for racks med oppgitt maxtall noder/ rack
	# @param noderPerRack max antall noder som kan plasseres i et rack
	def __init__(self, noderPerRack):
		self._racks = []
		self._noderPerRack = noderPerRack
	## Alternativ konstruktor for de som loser oppgave d). Kan ellers ignoreres
	## Leser data om regneklynge fra fil, bygger datastrukturen.
	# @param filnavn filene der dataene for regneklyngen ligger
#	def __init__(self, filnavn):
#		pass

	## Plasserer en node inn i et rack med ledig plass, eller i et nytt
	# @param node referanse til noden som skal settes inn i datastrukturen
	def settInnNode(self, node):
		#if len(self._racks)==0:
		#	self._racks.append(Rack(self._noderPerRack))

		for rack in self._racks:
			if rack.getAntNoder() < rack._maxnodes:
				rack.settInn(node)
				return

		self._racks.append(Rack(self._noderPerRack))
		self.settInnNode(node)
		#print(len(self._racks))
		#print(self.antProsessorer())
	## Beregner totalt antall prosessorer i hele regneklyngen
	# @return totalt antall prosessorer
	def antProsessorer(self):
		antall_prosessorer = 0
		for rack in self._racks:
			antall_prosessorer += rack.antProsessorer()
		return antall_prosessorer

	## Beregner antall noder i regneklyngen med minne over angitt grense
	# @param paakrevdMinne hvor mye minne skal noder som telles med ha
	# @return antall noder med tilstrekkelig minne
	def noderMedNokMinne(self, paakrevdMinne):
		nok_minne = 0
		for rack in self._racks:
			nok_minne += rack.noderMedNokMinne(paakrevdMinne)
		return nok_minne

	## Henter antall racks i regneklyngen
	# @return antall racks
	def antRacks(self):
		return len(self._racks)
