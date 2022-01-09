#I denne oppgaven skal du lage et program som holder styr over bursdager ved hjelp av lister.
#Lag en del der du spør om hvor mange bursdager brukeren har lyst til å taste inn
#så spør brukeren om å taste inn datoene og skriv dem ut
#Lag en rutine som som spør brukeren om de har lyst til å printe en spesifik persons bursdag der programmet slutter om de takker nei


bursdag_liste=[]
mengde=int(input("Hvor mange bursdager har du lyst til å taste inn?\n")) #bestemme hvor mange bursdager brukeren har lyst til å taste inn
for i in range(mengde):
    print("tast inn et navn og en bursdag (bare tall): ")
    bursdag_liste.append([input("Navn: "),int(input("Dag: ")),int(input("Månede: ")),int(input("År: "))])#Tar input for dag, månede og år og putter det i en liste

print("")
print("Alle bursdager:\n")

for i in range(len(bursdag_liste)):#printer ut alle bursdagene
    print(bursdag_liste[i][0]+":",str(bursdag_liste[i][1])+"."+str(bursdag_liste[i][2])+"."+str(bursdag_liste[i][3]))

#funksjon som inneholder en rutine for å finne en spesifik bursdag
def slutt_program():
    skrive_ut=input("Har du lyst til å skrive ut bursdagen til en spesifik person(y/n)?\n")
    if skrive_ut=="y" or "yes":
        lookup=input("Hvem da? ")
        for i in range(len(bursdag_liste)):#søker gjennom alle listene inni bursdag_liste for å se om den første verdien er lik bruker input
            if lookup==bursdag_liste[i][0]:
                print(str(bursdag_liste[i][0])+":",str(bursdag_liste[i][1])+"."+str(bursdag_liste[i][2])+"."+str(bursdag_liste[i][3]))
            else:
                print("Den personen er ikke i listen.")
        slutt_program()
    elif skrive_ut=="n" or "no":
        quit()#slutter programmet hvis brukeren ikke har lyst til å skrive noe ut
    else:
        print("Det forstod jeg ikke. La oss ta det igjen.") #hvis brukeren ikke har skrevet y eller n kjøres rutinen om igjen
        slutt_program()
slutt_program()#kjører rutinen
