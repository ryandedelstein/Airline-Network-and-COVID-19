import xlwt
from xlwt import Workbook
import json
import ast


def line_to_connectivity(line):
    outwards = line[:3]
    rest = line[4:]
    curr = ast.literal_eval(rest)
    return [outwards, curr]

def calculate_percent_diff(a, b):
    if a < b:
        c = a
        a = b
        b = c
    diff = a - b
    return diff / a






covid = open("covid_data.txt", "r")
line = covid.readline()
covid_data = {}
while line:
    covid_data[line[:3]] = float(line[4:])
    line = covid.readline()


  
# Workbook is created
wb = Workbook()
connectivity = wb.add_sheet("Connectivity")

file = open("connectivity.txt", "r")
line = file.readline()
connects = {}
while line:
    try:
        curr = line_to_connectivity(line)
        for i in curr[1]:
            connects[curr[0] + " " + i] = curr[1][i]
    except:
        print(line)
    line = file.readline()


conn_covid = {}
conn = {}
num = 1
for i in connects:
    first = i[:3]
    second = i[4:]
    connectivity.write(num, 1, first)
    connectivity.write(num, 2, second)
    connectivity.write(num, 3, connects[i])

    diff = calculate_percent_diff(covid_data[first], covid_data[second])
    connectivity.write(num, 4, diff)


    if connects[i] in conn_covid:
        conn[connects[i]] = conn[connects[i]] + 1
        conn_covid[connects[i]] = conn_covid[connects[i]] + diff
    else:
        conn_covid[connects[i]] = diff
        conn[connects[i]] = 1 

    num = num + 1

connectivity_summary = wb.add_sheet("Connectivity Summary")
num = 1
for i in conn_covid:
    connectivity_summary.write(num, 1, i)
    connectivity_summary.write(num, 2, conn_covid[i]/conn[i])
    num = num + 1



betweenness = wb.add_sheet("Betweenness")
between = {}
file = open("betweenness.txt")
line = file.readline()
while line:
    between[line[0:3]] = float(line[4:])
    line = file.readline()

num = 1
for j in between:
    betweenness.write(num, 1, j)
    betweenness.write(num, 2, between[j])
    betweenness.write(num, 3, covid_data[j])
    num = num + 1


centrality = wb.add_sheet("Centrality")
central = {}
file = open("centrality.txt")
line = file.readline()
while line:
    central[line[0:3]] = float(line[4:])
    line = file.readline()

num = 1
for j in central:
    centrality.write(num, 1, j)
    centrality.write(num, 2, central[j])
    centrality.write(num, 3, covid_data[j])
    num = num + 1


wb.save('Network_Project.xls')