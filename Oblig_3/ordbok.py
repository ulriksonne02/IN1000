#Dette programmet lager en ordbok som inneholder matvarer og priser, brukeren blir spurt to ganger om å legge til en matvare og en pris

#ordboken med matvarene og prisene blir definert
varer={"Melk":"kr 14.90","Brød":"kr 24.90","Yoghurt":"kr 12.90","Pizza":"kr 39.90"}
print(varer)
#En loop som kjører to ganger tar bruker input og for matvarer of pris og legger dem til ordboken
for i in range(2):
    ny_vare=input("Tast inn en ny vare")
    ny_pris=input("Tast inn en ny pris")
    varer.update([(ny_vare,ny_pris)])
#Ordboken printes
print(varer)
print(varer["Melk"])
