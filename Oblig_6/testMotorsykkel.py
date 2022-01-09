from motorsykkel import motorsykkel
#del 5 og 6
def hovedprogram():
    p1 = motorsykkel(10,"BMW","NO12345")
    p1.skrivUt()
#del 7
    p1.kjor()
    print(p1.hent_kilometerstand())
#del 8
hovedprogram()
