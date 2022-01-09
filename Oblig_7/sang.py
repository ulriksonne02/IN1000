#Denne filen inneholder en klasse som har metoder for å sjekke artist, tittel og begge samtidig.
#del 1
class Sang():
    def __init__(self,artist,tittel): #konstruktør
        self._artist = artist
        self._tittel = tittel
    def spill(self): #printer artist og tittel
        print("Spiller:",self._artist,"-",self._tittel)
    def sjekkArtist(self,artist): #sjekker artist ved å splitte ordene i en string og putte dem i en liste
        artist_parts = artist.split() #split mellomrom
        print(artist_parts)
        print(self._artist.split())
        for in_part in artist_parts:
            for  my_part in self._artist.split():
                if my_part == in_part:
                    return True
        return False
    def sjekkTittel(self,tittel): #Fungerer likt som sjekkArtist, men gjør det samme for tittelen
        tittel_parts = tittel.lower().split() #split mellomrom
        print(tittel_parts)
        print(self._tittel.lower().split())
        for in_part in tittel_parts:
            for  my_part in self._tittel.lower().split():
                if my_part == in_part:
                    return True
                    return False
    def sjekkArtistOgTittel(self,artist,tittel): #kjører både sjekkArtist og sjekkTittel
        if self.sjekkArtist(artist)==True and self.sjekkTittel(tittel)==True:
            return True
        else:
            return False
