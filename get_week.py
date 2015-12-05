F_in = open('data/trip_fare_6.csv', 'r')
F_out = open('data/trip_fare_6_9_15.csv', 'w')
header = F_in.readline()
new_header = ''.join([c for c in header if c != ' '])
F_out.write(new_header)

for line in F_in:
    medallion, hack_license, vendor_id, pickup_datetime, payment_type, fare_amount, surcharge, mta_tax, tip_amount, tolls_amount, total_amount = line.split(',')
    if pickup_datetime >= '2013-06-09 00:00:00' and pickup_datetime <= '2013-06-15 23:59:59':
        F_out.write(line)