#Dette programmet spør bruker om å taste inn ett navn og sted som så blir printet ut sammen med en melding.
#Denne rutinen blir definert som en funksjon, etter det kjøres den funksjonen tre ganger.

#Funksjonen NavnOgSted_rutine blir definert.
def NavnOgSted_rutine():
#Bruker input blir lagret i hver sin variabel.
    navn=input("Skriv inn navn: ")
    sted=input("Hvor kommer du fra? ")
#De blir printet ut sammen med en melding.
    print("Hei,",navn+"! Du er fra",sted+".")
#En ekstra linje blir printet slik at det blir litt mellomrom hver gang NavnOgSted_rutine kjøres.
    print("")

#for i in range(3): gjør at NavnOgSted_rutine kjøres tre ganger på rad.
for i in range(3):
    NavnOgSted_rutine()
