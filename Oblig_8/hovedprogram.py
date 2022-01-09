from rack import Rack
from regneklynge import Regneklynge
from node import Node
from datasenter import Datasenter

#oppgave 5
def hovedprogram():
    m1 = Datasenter() #gjør m1 til Datasenter objekt
    m1.lesInnRegneklynge("abel.txt") #leser inn abel
    print("ferdig med abel******************")
    m1.lesInnRegneklynge("saga.txt") #leser inn saga
    print("ferdig med saga*****************")
    m1.skrivUtAlleRegneklynger() #skriver ut alle detaljene i oppg 5
hovedprogram()
