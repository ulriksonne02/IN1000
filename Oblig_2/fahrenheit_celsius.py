#Dette programmet konverterer en gitt verdi i fahrenheit til celsius.

def temperatur_convert():
#Konverterer inputten fra string til integer.
    fahrenheit=int(input("Fahrenheit: "))
    fahrenheit_converted=((fahrenheit)-32)*5/9
    print("Fahrenheit kovertert til celsius blir:",fahrenheit_converted)
#Funksjonen kjøres.
temperatur_convert()
