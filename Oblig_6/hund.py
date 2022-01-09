#dett programmet er en klasse som har tre metoder

#del 1
class hund():
    def __init__(self,alder,vekt):
        self._alder = alder
        self._vekt = vekt
        self._metthet = 10
#del 2
    def skriv_ut(self):
        print("alder:",self._alder)
        print("vekt:",self._vekt)
        print("metthet:",self._metthet,"\n")
#del 3
    def spring(self):
        self._metthet -= 2
        if self._metthet < 5:
            self._vekt -= 2
#del 4
    def spis(self):
        self._metthet += 2
        if self._metthet > 7:
            self._vekt += 2
