#dette programmet består av en klasse som har en konstruktør og tre metoder

#del 1
class motorsykkel():
    def __init__(self,km,merke,registrering):
        self.km = km
        self.merke = merke
        self.registrering = registrering
#del 2
    def kjor(self):
        self.km = self.km+10
        return self.km
#del 3
    def hent_kilometerstand(self):
        return self.km
#del 4
    def skrivUt(self):
        print(self.merke,self.registrering,self.km)
