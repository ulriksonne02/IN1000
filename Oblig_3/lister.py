#programmet lager en liste, legger til et element
#programmet

#lag liste
tall_liste=[10,24,6]
#legg til en
tall_liste.append(700)
#print
print(tall_liste[0],tall_liste[2])

#navneliste
navn_liste=[]

#ta inn navn
for i in range(4):
    navn_liste.append(input("Skriv inn et navn"))
#sjekk om inputten er lik navnet mitt
if "Ulrik" in navn_liste:
    print("Du husket meg!")
#hvis ikke print dette
else:
    print("Glemte du meg?")


ny_tall_liste=[]
counter=0
product=1
#append summen og produktet til ny_tall_liste
for i in range(4):
    counter=counter+tall_liste[i]
    product=product*tall_liste[i]
ny_tall_liste.append(counter)
ny_tall_liste.append(product)


print(ny_tall_liste)
neo_tall_liste=[]
#den originale tall listen blir lagt til neo_tall_liste
for i in range(len(tall_liste)):
    neo_tall_liste.append(tall_liste[i])
#så blir summen og produktet lagt til
for i in range(len(ny_tall_liste)):
    neo_tall_liste.append(ny_tall_liste[i])
#print
print(neo_tall_liste)
#fjern summen og produktet
neo_tall_liste.pop(5)
neo_tall_liste.pop(4)
#print
print(neo_tall_liste)
