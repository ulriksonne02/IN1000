#Dette programmet summerer to tall, brukeren blir spurt om å taste inn en setning og så spør brukeren om å taste inn en bokstav for å se hvor mange ganger den bokstaven hender i setningen

setning=[]
#Del 1
def adder(tall1,tall2):#tar tall1 og tall2 som parametere
    print(tall1,"+",tall2,"=",tall1+tall2)

#tar tall som parametere
adder(1,6)
adder(11,3)

#Del 3

def tellForekomst(minTekst,minBokstav):
    teller=0

    for bokstav in minTekst:
        if bokstav == minBokstav:#hvis bokstaven er i strengen legges går teller opp med en
            teller = teller + 1
    return teller

#Dette er nå del 2
print(tellForekomst(input("Tast inn en setning.\n"),input("skriv en bokstav: ")))#printer tellForekomst med gitte parametere
