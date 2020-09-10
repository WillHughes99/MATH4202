import csv
import math
import random
from gurobipy import *


#Reading Data into file 
with open('Adjacency_Bloedel.csv', newline='') as f:
    reader = csv.reader(f)
    AdjacentStands = list(reader)

with open('StandArea_Bloedel.csv', newline='') as f:
    reader = csv.reader(f)
    StandArea = list(reader)

with open('StandVolume_Bloedel.csv', newline='') as f:
    reader = csv.reader(f)
    Volume = list(reader)
    
with open('StandRevenue_Bloedel.csv', newline='') as f:
    reader = csv.reader(f)
    Profit = list(reader)

#Data

numStands=45
#Period length (Years)
l = 10
#All data corresponds directly to how it was presented in the report
#Some data for Bloedel not available(e.g. age we only know the average age)
#Number of periods
T = range(3)
a = [int(StandArea[i][0]) for i in range(1,len(StandArea))]
age = {(t):[] for t in T}
for t in T:
    for i in range(1,len(StandArea)):
        age[t].append(43+l*t)
CAgeMin = 0
CAgeMax = 1000
MAgeMin = 40
Amax = 4
COmin = 1
COTmin = 15
p = {(t):[] for t in T}
for t in T:
    for i in range(0,len(Profit)):
        p[t].append(2500+float(Profit[i][t]))
        
v = {(t):[] for t in T}
for t in T:
    for i in range(0,len(Volume)):
        v[t].append(float(Volume[i][t]))
        
C = {t: [] for t in T}
for t in T:
    for i in range(0,numStands):
        if age[t][i]>CAgeMin:
            C[t].append(i)

pi = {i: [] for i in range(numStands)}
for i in range(numStands):
    for j in range(1,len(AdjacentStands)):
        if int(AdjacentStands[j][0])==i+1:
            pi[i].append(AdjacentStands[j][1])
        
#All other data now requires use of Tarjan's algorithm
Adj = {(t):[] for t in range(numStands)}
for j in range(numStands):
    for i in range(1,len(AdjacentStands)):
        if int(AdjacentStands[i][0])==j+1:
            Adj[j].append(int(AdjacentStands[i][1])-1)

#M = {t:[] for t in T}