#Dette programmet kjører 5 funksjoner, en som adderer, subtraherer, deler, konverterer tommer til cm og til slutt en som tar bruker input og kaller alle de forrige funksjonene.
#del 1
def addisjon(tall1,tall2):
    return tall1+tall2 #addering
#del 2
def subtraksjon(tall1,tall2):
    return tall1-tall2 #subtraksjon

def divisjon(tall1,tall2):
    return tall1/tall2 #divisjon
#del 3
def TommerTilFunksjon(antallTommer):
    assert antallTommer>0 #sjekk om antallTommer er mer en null eller ikke
    antallTommer=antallTommer*2.54
    return antallTommer
#del 4
def skrivBeregninger():
    tall1=input("skriv inn et tall 1: ") #ta input
    tall2=input("skriv inn et tall 2: ")
    if tall1.count("." or ",")>0: #hvis tall1 har punktum eller komma i seg er det en float
        tall1=float(tall1) #konverter strengen til float
    else:
        tall1=int(tall1) #hvis det bare er et vanlig tall, konverter strengen til integer
    if tall2.count("." or ",")>0: #repeter for tall2
        tall2=float(tall2)
    else:
        tall2=int(tall2)

    print(addisjon(tall1,tall2)) #print alle funksjonene
    print(subtraksjon(tall1,tall2))
    print(divisjon(tall1,tall2))
    print("Resultat:",TommerTilFunksjon(int(input("konvertering fra tommer til cm:\nSkriv inn et tall: "))))

print(addisjon(1,6))
print(subtraksjon(1,6))
print(TommerTilFunksjon(0.3))
print(skrivBeregninger())

#assert checks
assert addisjon(1,6)==1+6
assert addisjon(-2,-5)==(-2)+(-5)
assert addisjon(7,-4)==(7)+(-4)

assert subtraksjon(1,6)==1-6
assert subtraksjon(-2,-5)==(-2)-(-5)
assert subtraksjon(7,-4)==(7)-(-4)
