#Dette programmet finner en film med valgte sjangere

#definerer ordbok av filmer og sjanger
filmer={"Star Wars":["Sci-Fi","Action"],"Terminator":["Sci-Fi","Action"],"Lord of The Rings":["Fantasy"],"Die Hard":["Action"]}

#start
def finn_film():
    #skriv ut hvert filmnavn
    for i in filmer.keys():
        print(i)
    #Bruker input
    sjanger=input("Velg en film fra listen for å se sjangere\n")
    #Skriv ut sjanger til filmen
    if sjanger in filmer:
        print(filmer[sjanger])
#kjør
finn_film()
