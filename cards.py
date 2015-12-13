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

for i in range(2, 53, 2):
    print str(cards(i)) + ","