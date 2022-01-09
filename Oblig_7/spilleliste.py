from sang import Sang

class Spilleliste:
    def __init__(self, listenavn): #konstruktør
        self._sanger = []
        self._navn = listenavn
    def lesFraFil(self, filnavn): #legger alle sangene fra en fil til en spilleliste
        for line in open(filnavn):
            info = line.strip().split(";")
            self._sanger.append(Sang(info[0], info[1]))
    def leggTilSang(self, nySang): #legger til ny sang til listen
        self._sanger.append(nySang)
    def fjernSang(self, sang): #fjerner sang fra spillelisten
        self._sanger.remove(sang)
    def spillSang(self, sang): #spiller sang ved å bruke argument i spill() metoden i Sang
        sang.spill()
    def spillAlle(self): #spiller av hele spillelisten
        for i in self._sanger:
            i.spill()
    def finnSang(self, tittel): #går gjennom spillelisten og returner sang med samme tittel som argumentet
        for i in self._sanger:
            if i.sjekkTittel(tittel) == True:
                return i
        return None
    def hentArtistUtvalg(self, artistnavn): #returnerer sangene i listen for en gitt artist
        artistutvalg = []
        for i in self._sanger:
            if i.sjekkArtist(artistnavn):
                artistutvalg.append(i)
        return artistutvalg
