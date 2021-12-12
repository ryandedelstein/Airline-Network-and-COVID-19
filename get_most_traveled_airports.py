import pandas as pd

LEN_FLIGHTS = 18665

df = pd.read_csv("13410530_T_T100D_MARKET_US_CARRIER_ONLY.csv")
out_file1 = open("sorted_airports.txt", "w")
out_file2 = open("sorted_flights.txt", "w")

flights = {}

for i in range(LEN_FLIGHTS):
    curr = df["ORIGIN"][i] + " " + df["DEST"][i]
    curr_pass = df["PASSENGERS"][i]

    if curr in flights:
        flights[curr] = flights[curr] + curr_pass
    else:
        flights[curr] = curr_pass

import operator
sorted_flights = sorted(flights.items(), key=operator.itemgetter(1))

airports = {}
for i in flights:
    curr = i.split(" ")
    if curr[0] in airports:
        airports[curr[0]] = airports[curr[0]] + flights[i]
    else:
        airports[curr[0]] = flights[i]


sorted_airports = sorted(airports.items(), key=operator.itemgetter(1))

for i in sorted_flights:
    s = i[0] + " " + str(i[1]) + "\n"
    out_file2.write(s)

for i in sorted_airports:
    s = i[0] + " " + str(i[1]) + "\n"
    out_file1.write(s)