#Dette programmet kjører to funksjoner: en som teller bokstavene i et en teksstreng og en som legger hvert ord i en ordbok sammen med hvor mange ganger det ordet er i setningen.

#Del 1
def antall_bokstaver(ord):
    antall=ord.split() #split ordene/bokstavene fra ord
    return len(antall) #returnerer antallet

#Del 2
def ordbok_funksjon(min_tekst):
    ordbok1={}
    for ord in min_tekst.split(): #splitter ordene og legger dem til en ordbok
        if ord in ordbok1:
            ordbok1.update({ord:ordbok1.get(ord)+1})#oppdaterer verdien til ord som allerede er i ordboken plus en
        else:
            ordbok1.update({ord:1}) #legger til en splittede strengen
    return ordbok1

#Del 3
input_1=input("Skriv en setning: ")
print("Det er",antall_bokstaver(input_1),"ord i setningen din.")
for i in ordbok_funksjon(input_1): #printer hvert ord i ordboken, hvor mange ganger de forekommer og hvor mange bokstaver det er i ordet
    print("Ordet","'"+str(i)+"'","Forekommer",ordbok_funksjon(input_1).get(i),"ganger, og det er",len(i),"bokstaver i ordet")
