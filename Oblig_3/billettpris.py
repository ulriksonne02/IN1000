#Dette programmet kjører en prosedyre som spør hvor gammel brukeren er og deretter gir dem en billettpris basert på aldersgruppe.


def billett_kontroll():
#bruker input blir lagret i variablen alder
    alder=int(input("Du har lyst til å kjøpe billett. Hvor gammel er du?"))
    billettpris=0
#hvis alder er lik eller mindre enn 17 får brukeren barnebillett
    if alder <= 17:
        billettpris=30
#hvis brukeren er 63 eller mer får han pensjonistbillett
    elif alder >= 63:
        billettpris=35
#fhis brukeren er over 17 får han vanlig billett
    elif alder > 17:
        billettpris=50
    print("Billetprisen er",str(billettpris)+".")
#funksjonen kjøres
billett_kontroll()
