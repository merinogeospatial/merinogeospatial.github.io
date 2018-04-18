import csv
import smtplib
from geopy.geocoders import GoogleV3

print ("****Start****")

# Ask inputs
CSV_IN = input("Enter input CSV's name: ")
CSV_OUT = input("Name your output CSV: ")
LocationSet = input("Enter the location, format (RALEIGH NC): ")
GoogleKey = input("Enter your Google API key: ")


f = open(CSV_IN + ".csv")  
csv_f = csv.reader(f)

Meter = []
Address = []
Usage = []
X_coord = []
Y_coord = []


for row in csv_f:
    Address.append(
        row[1] + LocationSet ) 
    Meter.append(row[0])
    Usage.append(row[2])

csv_out = open( CSV_OUT + ".csv", 'w')  

headers = "OID" + "," + "METER" + "," + "ADDRESS" + "," + "USAGE" + "," + "YCOORD" + "," + "XCOORD" + "\n"
out = headers
csv_out.write(out)


for i in range(len(Address)):

    g = GoogleV3(api_key=GoogleKey)  
    add = g.geocode(str(Address[i]), exactly_one=True, timeout=10)
    if add is not None:
        X_coord.append(add.latitude)
        Y_coord.append(add.longitude)
        print ("Grabbing address and assigning latitude/longitude for row: ") + str(i)
        out = str(i) + "," + Meter[i] + "," + Address[i] + "," + Usage[i] + "," + str(Y_coord[i]) + "," + str(
            X_coord[i]) + "\n"
        csv_out.write(out)
        print ("Writing row " + str(i) + " to csv")
    else:
        Y_coord.append("X")
        X_coord.append("X")
        print ("Grabbing address and assigning latitude/longitude for row: ") + str(i)
        out = str(i) + "," + Meter[i] + "," + Address[i] + "," + Usage[i] + "," + str(Y_coord[i]) + "," + str(
            X_coord[i]) + "\n"
        csv_out.write(out)
        print ("Writing row " + str(i) + " to csv")
        
csv_out.close()
f.close()
print ("DONE")
