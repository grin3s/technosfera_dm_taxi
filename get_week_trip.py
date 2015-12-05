F_in = open('data/trip_data_6.csv', 'r')
F_out = open('data/trip_data_6_9_15.csv', 'w')
header = F_in.readline()
new_header = ''.join([c for c in header if c != ' '])
F_out.write(new_header)

for line in F_in:
    medallion, hack_license, vendor_id, rate_code, store_and_fwd_flag, pickup_datetime, dropoff_datetime, passenger_count, trip_time_in_secs, trip_distance, pickup_longitude, pickup_latitude, dropoff_longitude, dropoff_latitude = line.split(',')
    if pickup_datetime >= '2013-06-09 00:00:00' and pickup_datetime <= '2013-06-15 23:59:59':
        F_out.write(line)

print "Finished"