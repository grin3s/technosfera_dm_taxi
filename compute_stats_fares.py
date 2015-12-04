from tables import *

h5file = open_file("data/trip_fare_1.h5", mode = "r")

table = h5file.root.fares

d = dict()
for row in table.iterrows():
    type = row["payment_type"]
    if type in d:
        d[type] += 1
    else:
        d[type] = 1

h5file.close()



