import pandas as pd

n1 = n3 = 2
n2 = 1
m = 4

inputData = pd.read_csv("inputData.csv", index_col="q0")

bq0 = []
for i in inputData[:-m]:
    bq0 += [(max(inputData[i]) + min(inputData[i]))/2]

for i in inputData:
    inputData[i] = (inputData[i] - min(inputData[i])) / (max(inputData[i]) - min(inputData[i]))

print(bq0)
print(inputData)
