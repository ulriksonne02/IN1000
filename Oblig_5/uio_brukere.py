#Dette programmet er bygget opp av 3 funksjoner en som lager brukernavn, en som lager eposter og en som skriver ut de epostene. Til slutt er det en loop som lar brukeren legge til brukere ved hjelp av de nevnte funksjonene.
#del 1
def lagBrukernavn(navn): #funksjon som lager brukernavn
    navn = navn.lower()
    navn = navn.split()
    brukernavn=navn[0]+navn[1][:1]
    return brukernavn
#del 2
def lagEpost(brukernavn,suffiks): #lager epost ved å kombinere brukernavn fra den forrige funksjonen med "@"
    return brukernavn+"@"+suffiks
#del 3
def skrivUtEposter(brukere):
    for elementer in brukere:
        return (lagEpost(elementer,brukere[elementer]))
#testing
navn=input("Tast inn et navn (fornavn etternavn): ")
addresse=input("Tast inn suffiks (det som skal komme etter @): ")
print(lagEpost(lagBrukernavn(navn),addresse))
print(skrivUtEposter({"olan":"ifi.uio.no","karin":"student.matnat.uio.no"}))

min_ordbok={}
turn_off=True
#del 4
while turn_off==True: #Loop som lar bruker legge til brukere
    bruker_input1=input("tast i for å legge til bruker, tast p for å printe epostaddresser: ")
    if bruker_input1=="i":
        min_ordbok.update([(lagBrukernavn(input("skriv navn: ")),input("tast inn suffiks: "))])
    elif bruker_input1=="p":
        print(skrivUtEposter(min_ordbok))
    else:
        turn_off=False
