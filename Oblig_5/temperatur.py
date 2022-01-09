import csv
#max_daily_temperature_2018.csv
#max_temperatures_per_month.csv
#open("") as f:



def funksjon(filnavn):
    with open(filnavn,newline="") as csvfile:
        ordbok={}
        splitord=""
        spamreader = csv.reader(csvfile, delimiter=' ', quotechar='|')
        for row in spamreader:
            #print(', '.join(row))
            splitord=row[0].split(",")
            #splitord.split()
            #for i in range(len(csvfile.readlines())):

            #ordbok.update(splitord[0]:splitord[1])
            ordbok.update({splitord[0]:splitord[1]})
            ordbok.update({splitord[0]:float(splitord[2])})
            #print(type(splitord))
            print(ordbok.values())
    return ordbok
    print()
print(funksjon("max_daily_temperature_2018.csv"))
