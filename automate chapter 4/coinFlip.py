import random
currentStreak = []

def cointoss():
    for experimentNumber in range(10000):
        cointoss = random.randint(0,1)
        currentStreak.append(cointoss)
        # Code that checks if there is a streak of 6 heads or tails in a row.
    return currentStreak

def run():
    result = cointoss()
    streak(currentStreak)
    #print(streak(currentStreak))
def streak(currentStreak):
    count = 0
    current_Streak_Len = len(currentStreak)
    numberOfStreaks = 0
    for coin in range(0, current_Streak_Len - 1):
        currentCoin = currentStreak[coin]
        next_coin = currentStreak[coin + 1]
        if currentCoin == 0:
            count+=1
            if currentCoin != next_coin:
                count = 0
            elif currentCoin == next_coin:
                count+=1
                if count == 6:
                    numberOfStreaks+=1
                    count = 0
        elif currentCoin == 1:
            count+=1
            if currentCoin != next_coin:
                count = 0
            elif currentCoin == next_coin:
                count+=1
                if count == 6:
                    numberOfStreaks+=1
                    count = 0
    print('Chance of streak: %s%%' % (numberOfStreaks / 1000.0))
    return numberOfStreaks

run()
