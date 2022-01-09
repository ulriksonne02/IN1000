#Dette programmet kjører en undesøkelse som spør brukeren om klesplagg og reismål som så printer det brukeren har tastet inn

reiseplan=[]
steder=[]
klesplagg=[]
avreisedatoer=[]
print("Tast inn 5 forskjellige reisemål, klesplagg og avreisedatoer")
#del 1 og del 2
for i in range(5): #Ber brukeren om å taste inn 5 forskjellige steder, klesplagg og avreisedatoer
    steder.append(input("Sted"))
    klesplagg.append(input("Klesplagg"))
    avreisedatoer.append(input("Avreisedato"))

#del 3
reiseplan.append(steder) #legger alt til hovedlisten
reiseplan.append(klesplagg)
reiseplan.append(avreisedatoer)

#del 4
for i in range(len(reiseplan)): #printe hovedlisten
    print(reiseplan[i])

#del 5
def indeks_input(): #funksjon som printer en gitt verdi i en gitt lisste
    liste_indeks1=int(input("tast inn et tall fra 0 til 2"))
    liste_indeks2=int(input("tast inn et tall fra 0 til 4"))
    if liste_indeks1>2 or liste_indeks1<0 or liste_indeks2>4 or liste_indeks2<0: #hvis input er utenfor grensen gir den en feilmelding
        print("ugyldig input")
        indeks_input()
    else:
        print(reiseplan[liste_indeks1][liste_indeks2])#print avreisedato
indeks_input()
