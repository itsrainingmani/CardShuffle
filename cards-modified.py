#from __future__ import division
import csv

def homogenous(decks,n):
    firstel = decks[0][0]
    ishomo = True
    for i in range(0,n):
        if decks[i][0] != firstel:
            ishomo = False
    return ishomo

def cards(k):
    deck = [[1,0] for i in range(0,k)]
    #print deck

    num_step = 0

    half1 = deck[:k/2]
    half2 = deck[k/2:]
    for i in range(0,len(half2)):
        temp = half2[i][0]
        half2[i][0] = half2[i][1]
        half2[i][1] = temp
    half2.reverse()
    deck[::2] = half2
    deck[1::2] = half1
    #print deck
    num_step += 1

    while (homogenous(deck,k) == False):
        half1 = deck[:k/2]
        #print half1
        half2 = deck[k/2:]
        #print half2
        for i in range(0,len(half2)):
            temp = half2[i][0]
            half2[i][0] = half2[i][1]
            half2[i][1] = temp
        half2.reverse()
        deck[::2] = half2
        deck[1::2] = half1
        num_step += 1
        #print deck

    return num_step

num = []

for i in range(3, 10001, 1):
    num.append([i, cards(i)])

with open("Card-10000.csv","a+") as csvdata:
    cardwriter = csv.writer(csvdata, delimiter=',')
    for n in num:
        cardwriter.writerow(n)
'''

with open("Card-Same-Odd.csv","a+") as csvdata:
    cardwriter = csv.writer(csvdata, delimiter=',')
    for i in range(0,len(num)):
        if (num[i][0] == num[i][1]):
            cardwriter.writerow(num[i])

with open("Card-Diff-Odd.csv","a+") as csvdata:
    cardwriter = csv.writer(csvdata, delimiter=',')
    for i in range(0,len(num)):
        if (num[i][0] != num[i][1]):
            cardwriter.writerow(num[i])


with open("Card-Even.csv",'rb') as csvdata:
    cardreader = csv.reader(csvdata)
    for row in cardreader:
        temp = [int(row[0]), int(row[1])]
        num.append(temp)

#print num

with open("Card-0.8-Odd.csv","wb") as csvdata:
    cardwriter = csv.writer(csvdata, delimiter=',')
    for i in range(0,len(num)):
        if ((float(num[i][1])/num[i][0]) >= (0.78) and (float(num[i][1])/num[i][0]) <= (0.98)):
            cardwriter.writerow(num[i])


with open("Card-0.3-Odd.csv","wb") as csvdata:
    cardwriter = csv.writer(csvdata, delimiter=',')
    for i in range(0,len(num)):
        if ((float(num[i][1])/num[i][0]) >= (0.32) and (float(num[i][1])/num[i][0]) <= (0.34)):
            cardwriter.writerow(num[i])

with open("Card-0.6-Odd.csv","wb") as csvdata:
    cardwriter = csv.writer(csvdata, delimiter=',')
    for i in range(0,len(num)):
        if ((float(num[i][1])/num[i][0]) >= (0.65) and (float(num[i][1])/num[i][0]) <= (0.67)):
            cardwriter.writerow(num[i])


with open("Card-0.5-Odd.csv","wb") as csvdata:
    cardwriter = csv.writer(csvdata, delimiter=',')
    for i in range(0,len(num)):
        if ((float(num[i][1])/num[i][0]) >= (0.45) and (float(num[i][1])/num[i][0]) <= (0.55)):
            cardwriter.writerow(num[i])
'''
