import csv 

file = open("top10.csv", "r") #rename file to match name of csv file containing data
data = csv.reader(file)
datalists = list(data)
print(datalists)
del datalists[0] #deletes the header row
print(datalists)

found = False
tally = []

for row in datalists:
    for j in range(1,len(row)): # skips the timestamp column
        name= row[j]
        found = False
        score = (16-j) #change to 15 if timetsamp column isnt in data
        for k in range(len(tally)):
            if tally[k][0] == row[j]:
                current = tally[k][1]
                tally[k][1] += score
                found = True
        if found == False:
            tally.append([name,score])
            

print("Here's the tally")
print(tally)

tally.sort(key=lambda x: x[1],reverse = True)
for i in range(10):
    print("And in the number " + str(i+1) + " position, we have " + str(tally[i][0]) + " with " + str(tally[i][1]) + " points!")

