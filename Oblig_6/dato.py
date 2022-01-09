class dato():
    def __init__(self, nyDag,nyMaaned,nyttAar):
        self._nyDag = nyDag
        self._nyMaaned = nyMaaned
        self._nyttAar = nyttAar
    def les_aar(self):
        return self._nyttAar
    def skriv_ut():
        return(str(self._nyDag)+"."+str(self._nyMaaned)+"."+self._nyttAar)
    def dag_sjekk():
        if self._nyDag==1:
            
