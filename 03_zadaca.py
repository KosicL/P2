from csv import reader
# open file in read mode
with open('rezultati.csv', 'r') as read_obj:
    # pass the file object to reader() to get the reader object
    csv_reader = reader(read_obj)
    # Get all rows of csv from csv_reader object as list of tuples
    rezultati = list(map(tuple, csv_reader))
    # display all rows of csv
    # print(rezultati)
novi_rezultati = sorted(rezultati, key=lambda x: x[1])
print(novi_rezultati)
rjecnik = {"Nedovoljan": 0, "Dovoljan": 0, "Dobar": 0, "Vrlo dobar": 0, "Izvrstan": 0}
for rezultat in rezultati:
    if (int(rezultat[2]) < 50):
        rjecnik["Nedovoljan"]+=1
    elif (50 <= int(rezultat[2]) < 65):
        rjecnik["Dovoljan"]+=1
    elif (65 <= int(rezultat[2]) < 80):
        rjecnik["Dobar"]+=1
    elif (80 <= int(rezultat[2]) < 90):
        rjecnik["Vrlo dobar"]+=1
    else:
        rjecnik["Izvrstan"]+=1

print(rjecnik)