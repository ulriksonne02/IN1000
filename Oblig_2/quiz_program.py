#Oppgavetekst:
#Lag ett quiz program som er skrevet på en pen og elegant måte
#Dette programmet er en quiz der brukeren skal kunne hovedstaten til ti forskjellige land
#Gjør bruk av nøstede lister

#En liste med nøstede lister inni seg, dette gjøres slik at koden blir fin og ryddig senere
land_og_by_liste=[
["Sveits","Bern"],
["Spania","Madrid"],
["Hviterusland","Minsk"],
["Argentina","Buenos Aires"],
["Tyrkia","Ankara"],
["Afghanistan","Kabul"],
["Serbia","Beograd"],
["Hellas","Athen"],
["Luxembourg","Luxembourg"],
["Nepal","Katmundu"]
]

#Quizen befinner seg inni en funksjon som går gjennom de samme stegene ti ganger
def quiz_rutine():
    print("Velkommen til en quiz der du skal kunne hovedstaten til 10 forskjellige land. Husk å stave ")
    poeng=0
#Prosessen kjøres ti ganger på rad, en gang per land
    for i in range(10):
#I stedet for å skrive hvert spørsmål på sin egen linje manuelt bruker jeg heller triks for å gjøre jobben for meg
#Dette har jeg oppnåd ved å legge landet og den korresponderende hovedstaten sammen i en nøstet liste som befinner seg inni den øvre listen land_og_by_liste
        print("Hva er hovedstaten i",land_og_by_liste[i][0]+"?")
        svar=input()
#Siden jeg la hvert land og sin korresponderende hovedstat i nøstede lister betyr det at jeg kan enkelt bruke den samme linjen med kode om igjen bare ved å bevege med oppover i de nøstede listene
        if svar==land_og_by_liste[i][1]:
            print("Riktig!")
#Poeng teller går opp hver gang man skriver riktig svar
            poeng=poeng+1
        else:
            print("Feil!")
#På slutten, printer den hvor mange poeng du fikk
    print("Du fikk",str(poeng),"ut av 10 poeng.")

#Quizen kjøres
quiz_rutine()
