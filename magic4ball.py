import random


def getAnswer(answerNumber):
    if answerNumber == 1:
        return "One and only"
    elif answerNumber == 2:
        return "Two Sure"
    elif answerNumber == 3:
        return ('Three Little Birds')
    elif answerNumber == 4:
        return "Four Oranges"


value = random.randint(1, 4)
answer = getAnswer(value)
print(answer)
