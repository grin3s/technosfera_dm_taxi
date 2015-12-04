from tables import *
import numpy as np

h5file = open_file("data/trip_fare_1.h5", mode = "r")

table = h5file.root.fares

#
#d = dict()
#for row in table.iterrows():
#    type = row["payment_type"]
#    if type in d:
#        d[type] += 1
#    else:
#        d[type] = 1

class Histogram(object):
    def __init__(self, **kwargs):
        self.delta = kwargs["delta"]
        self.cur_length = 0
        self.bins = np.array([])

    def insert_value(self, val):
        bin_idx = int(val / self.delta)
        if bin_idx >= self.cur_length:
            self.cur_length = bin_idx + 1
            self.bins.resize(self.cur_length)

        self.bins[bin_idx] += 1

h = Histogram(delta=0.1)

for row in table.iterrows():
    fare = row["total_amount"]
    h.insert_value(fare)

print "finished"

h5file.close()



