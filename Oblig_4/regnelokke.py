#Dette programmet kjører en while løkke som tar input fra brukeren og sjekker om det er null eller ikke, hvis det er null slutter while løkken.
#Alle tallene som brukeren skriver inn blir lagret i en liste, den listen blir printet ut, så blir summen av listen og det høyeste og laveste tallet fra listen


ozymandias=[]
minSum=0

største_tall=0

while True:
    intall = int(input("skriv tall"))
    if intall == 0:
        break
    else:
        ozymandias.append(intall)

#en for løkke som printer hvert tall i listen
for i in range(len(ozymandias)):
    print(ozymandias[i],"\n")
    minSum += ozymandias[i]
#summen av alle tallene i listen
print("summen av alle tallene i listen er",str(minSum))
#en for løkke som finner det største tallet i listen
for i in range(len(ozymandias)):
    if ozymandias[i]>største_tall:
        største_tall=ozymandias[i]

print("det største tallet i listen er",str(største_tall))
#en for løkke som finner det minste tallet i listen
minste_tall = ozymandias[0]
for i in range(len(ozymandias)):
    if ozymandias[i]<minste_tall:
        minste_tall=ozymandias[i]
print("det minste tallet i listen er",str(minste_tall))
