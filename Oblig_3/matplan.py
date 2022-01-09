#Dette programmet er en ordbok med navn der brukeren kan taste inn et navn for å se matplanen deres.

matplan={"Marcus Aurelius":["Cuban sandwich","Banan split","Posca"],"William Shakespear":["Brød","Cheddar","English Pudding"],"Mahatma Gandhi":["Curry","Linsesuppe","Naanbrød"]}

#Funksjonen
def jeg_elsker_funksjoner():
    print(matplan.keys())
    navn=input("Tast inn navnet til en beboer for å se matplanen deres")
    if navn in matplan:
        print("Her er matplanen:"matplan[navn])
    else:
        print("Denne personen bor ikke på sykehjemmet")
        jeg_elsker_funksjoner()
jeg_elsker_funksjoner()

#a)ordbok, om den skal relatere til noe (passord,brukerid, etc), mengde om bare brukernavn
#b)ordbok
#c)mengde
#d)ordbok, hvis relatert til individuelle gjester, hvis ikke, mengde
