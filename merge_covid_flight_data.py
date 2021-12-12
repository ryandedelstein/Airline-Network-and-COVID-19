import pandas as pd

LEN_FLIGHTS = 18665
LEN_COVID = 1048576

flights = pd.read_csv("13410530_T_T100D_MARKET_US_CARRIER_ONLY.csv")
covid = pd.read_csv("published_PUBLIC_COVID-19-Activity_1633284109_COVID-19_Activity.csv")

# get covid data by city
covid_by_city = {}
for i in range(LEN_COVID):
    curr_city = covid["STATE"][i]
    curr_case_rate = covid[]