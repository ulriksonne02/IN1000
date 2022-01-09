from regneklynge import Regneklynge
from node import Node
from rack import Rack
class Datasenter:

    ## Oppretter et datasenter
    #
    def __init__(self):
        self._max_noder_per_rack = 0
        self._regneklynger = {}

    ## Leser inn data om en regneklynge fra fil og legger
    # den til i ordboken
    # @param filnavn filene der dataene for regneklyngen ligger
    def lesInnRegneklynge(self, filnavn):
        with open(filnavn) as f: #åpner fil
            teller = 0 # teller som går opp hver gang for loopen slutter
            for line in f.readlines(): # for hver linje
                if teller == 0: # hvis teller er 0 sett max nodes til line og lag regneklynge objekt i self._regneklynger ordboken
                    self._max_noder_per_rack = int(line)
                    temp_klynge = Regneklynge(self._max_noder_per_rack)
                else: #for de to neste linjene split de tre tallene inn i en liste
                    split_line = line.split()
                    for i in range(len(split_line)):
                        split_line[i] = int(split_line[i])
                    for node in range(split_line[0]): # putt

                        temp_klynge.settInnNode(Node(split_line[1],split_line[2]))
                        #debug


                teller += 1
            self._regneklynger.update({filnavn.strip(".txt"):temp_klynge})

    ## Skriver ut informasjon om alle regneklyngene
    #
    def skrivUtAlleRegneklynger(self):
        for keys in self._regneklynger:
            print(keys)
            self.skrivUtRegneklynge(keys)

    ## Skriver ut informasjon om en spesifikk regeklynge
    # @param navn navnet på regnekyngen
    def skrivUtRegneklynge(self,klyngenavn):
        print("antall racks: " , self._regneklynger[klyngenavn].antRacks())
        print("antall noder: " , self._regneklynger[klyngenavn].antProsessorer())
        print("ant noder med mer en 32gb minne: " , self._regneklynger[klyngenavn].noderMedNokMinne(32))
        print("ant noder med mer en 64gb minne: " , self._regneklynger[klyngenavn].noderMedNokMinne(64))
        print("ant noder med mer en 128gb minne: " , self._regneklynger[klyngenavn].noderMedNokMinne(128))
