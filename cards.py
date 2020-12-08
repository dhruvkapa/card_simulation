from random import randint

def drawcards():
    firstCard = randint(1,14)
    secondCard = randint(1,14)

    if firstCard >= secondCard:
        return firstCard,secondCard
    elif firstCard < secondCard:
        return secondCard,firstCard

generateHumanCards = list(drawcards())
generateComputerCards = list(drawcards())


def cards2str(card):
    i = 0
    while i < len(card):
        if int(card[i]) >= 10:
            if int(card[i]) == 11:
                card[i] = 'J'
            elif int(card[i]) == 12:
                card[i] = 'Q'
            elif int(card[i]) == 13:
                card[i] = 'K'
            elif int(card[i]) == 14:
                card[i] = 'A'
        i+=1

    return card


def printhand(human,computer) -> None:
    print("[{}] [{}]".format(human[0],human[1]))

    print("[{}] [{}]".format(computer[0],computer[1]))


#Check if there is a pair
#If not, then check which card is greater, whether it is in humanCards or computerCards
def printoutcome(humanCards,computerCards):
    humanWin = "Human Wins!"
    computerWin = "Computer Wins!"

    if humanCards[0] == humanCards[1] and computerCards[0] != computerCards[1]:
        return humanWin

    elif humanCards[0] != humanCards[1] and computerCards[0] == computerCards[1]:
        return computerWin

    elif int(humanCards[0]) > int(computerCards[0]):
        return humanWin

    elif int(humanCards[0]) < int(computerCards[0]):
        return computerWin


printoutcome_result = printoutcome(generateHumanCards,generateComputerCards)



print(printhand(cards2str(generateHumanCards),cards2str(generateComputerCards)))
print(printoutcome_result)


