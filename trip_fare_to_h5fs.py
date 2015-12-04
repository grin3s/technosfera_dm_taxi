from tables import *

class TripFare(IsDescription):
    medallion = StringCol(32)
    hack_license = StringCol(32)
    vendor_id = StringCol(3)
    pickup_datetime = StringCol(19)
    payment_type = StringCol(3)
    fare_amount = Float32Col()
    surcharge = Float32Col()
    mta_tax = Float32Col()
    tip_amount = Float32Col()
    tolls_amount = Float32Col()
    total_amount = Float32Col()


F = open('data/trip_fare_1.csv', 'r')
F.readline()
h5file = open_file("data/trip_fare_1.h5", mode = "w", title = "Trip Fare 1")
root_group = h5file.root
table = h5file.create_table(root_group, 'fares', TripFare, "Trip Fares")
row = table.row

i = 1
for line in F:
    medallion, hack_license, vendor_id, pickup_datetime, payment_type, fare_amount, surcharge, mta_tax, tip_amount, tolls_amount, total_amount = line.split(',')
    row["medallion"] = medallion
    row["hack_license"] = hack_license
    row["vendor_id"] = vendor_id
    row["pickup_datetime"] = pickup_datetime
    row["payment_type"] = payment_type
    row["fare_amount"] = fare_amount
    row["surcharge"] = surcharge
    row["mta_tax"] = mta_tax
    row["tip_amount"] = tip_amount
    row["tolls_amount"] = tolls_amount
    row["total_amount"] = total_amount

    row.append()

    if i % 100000 == 0:
        table.flush()
        print "Row {0} saved".format(i)

    i += 1

table.flush()
F.close()
h5file.close()