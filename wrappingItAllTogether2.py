import random

name = input("What's your name: ")

correctAnswers = 0

for x in range(0, 10):

    if correctAnswers>=1:
        print("Correct Answers: ", correctAnswers)
    
    op = random.randrange(0,3) # random values for oporators

    randomNumber1 = random.randrange(1,10) # generating random numbers
    randNum1 = int(randomNumber1)

    randomNumber2 = random.randrange(11,20)
    randNum2 = int(randomNumber2)

    if op == 0:

        print(randNum2,"+",randNum1)

        rightAnswer = randNum2 + randNum1
    
    if op == 1:

        print(randNum2,"-",randNum1)

        rightAnswer = randNum2 - randNum1
    
    if op == 2:

        print(randNum2,"x",randNum1)

        rightAnswer = randNum2 * randNum1

    answer = input("input answer: ")

    while answer.isnumeric()== False or int(answer)!=rightAnswer:
        print("wrong, try again")
        answer = input("input answer: ") #this will loop back if they user gets the answer wrong

    correctAnswers+=1

    print("Great")

if correctAnswers == 10:
    print("Good job", name,"! You got 10 correct answers!")