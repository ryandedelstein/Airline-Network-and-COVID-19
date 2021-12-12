import pandas as pd

LEN = 18665

df = pd.read_csv("13410530_T_T100D_MARKET_US_CARRIER_ONLY.csv")

flights = {}

for i in range(LEN):
    curr = df["ORIGIN"][i] + " " + df["DEST"][i]
    curr_pass = df["PASSENGERS"][i]

    if curr in flights:
        flights[curr] = flights[curr] + curr_pass
    else:
        flights[curr] = curr_pass



out = open("flights.txt", "w")

for i in flights:
    out.write(i)
    out.write(" ")
    out.write(str(flights[i]))
    out.write("\n")