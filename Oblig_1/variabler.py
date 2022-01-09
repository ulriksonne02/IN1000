#dette programmet spør brukeren om å skrive to forskjellige navn som blir deretter lagt sammen
#to tall blir definert, etter det blir difernansen mellom dem regnet ut

#inputten lagres i navn
navn=input("Hva heter du?")
print("Hei",navn)

#hvert tall defineres i hver sin variabel og så printet
tall1=42
tall2=32
print(tall1)
print(tall2)
#differansen mellom dem blir regnet ut og printet
tall3=tall1-tall2
print("Differanse: ",tall3)

#ny input blir lagret i NyttNavn
NyttNavn=input("Oppgi et nytt navn")
sammen=navn+NyttNavn
print(sammen)
sammen=navn+" og "+NyttNavn
print(sammen)
