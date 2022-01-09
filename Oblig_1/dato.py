#dette programmet spør brukeren om å taste inn to forskjellige datoer
#brukeren blir så fortalt om datoene kommer i riktig rekkefølge

#spør bruker om å taste inn dato
print("Tast inn en dato i riktig rekkefølge.")

#inputten blir konvertert fra string til integer
dag1=int(input("Dag?"))
månede1=int(input("Månede?"))
print("Tast inn en dato til.")
dag2=int(input("Dag?"))
månede2=int(input("Månede?"))


#sammenligning av de to datoene ville ikke fungert hvis de ikke var integer
#hvis måneden i månede2 er høyere kan den ikke være i feil rekkefølge
if månede1 < månede2:
    print("Riktig rekkefølge!")
#hvis måneden er lik må vi sjekke om dagen i den andre datoen som brukeren skrev inn kom før eller etter den første
if månede1 == månede2:
    if dag1 < dag2:
        print("Riktig rekkefølge!")
    elif dag1==dag2:
        print("Samme dato!")
    elif dag1>dag2:
        print("Feil rekkefølge!")
#hvis måneden i den andre datoen er mindre må den nødvendigvis være i feil rekkefølge
elif månede1 > månede2:
        print("Feil rekkefølge!")
