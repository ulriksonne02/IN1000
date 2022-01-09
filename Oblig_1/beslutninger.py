#Programmet spør brukeren om de har lyst på en brus

#tastatur input til brukeren blir lagret i variabelen lystpåbrus
lystpåbrus=input("Har du lyst på en brus?(ja/nei)")

#Skjører en if statement der den printer svar på ja eller nei
if lystpåbrus=="ja":
    print("Her har du en brus!")
elif lystpåbrus=="nei":
    print("Den er grei.")
#hvis noe annet enn ja eller nei blir skrevet printer den ut dette
else:
    print("Det forstod jeg ikke helt.")
