import random
playerWins = 0
computerWins = 0

while playerWins < 1 or computerWins < 1:
    print("This is a Rock, Paper, Scissors game. You will input number 1 for Rock, 2 for Paper, or 3 for Scissor.")
    numberInput = input("Input your number:")
    number = int(numberInput)
    if number < 1 or number > 3:
        print("Invalid Number")
    computerInput = random.randrange(1,3)
    computerNumber = int(computerInput)
    if number == 1 and computerNumber == 3:
        print("You picked rock and the computer picked scissors. You Win!")
        playerWins += 2
    if number == 1 and computerNumber == 2:
        print("You picked rock and the computer picked paper. You Lose!")
        computerWins += 2
    if number == 1 and computerNumber == 1:
        print("You picked rock and the computer picked rock. Nobody Wins!")
    if number == 2 and computerNumber == 3:
        print("You picked paper and the computer picked scissors. You Lose!")
        computerWins += 2
    if number == 2 and computerNumber == 2:
        print("You picked paper and the computer picked paper. Nobody Wins!")
    if number == 2 and computerNumber == 1:
        print("You picked paper and the computer picked rock. You Win!")
        playerWins += 2
    if number == 3 and computerNumber == 3:
        print("You picked scissors and the computer picked scissors. Nobody Wins!")
    if number == 3 and computerNumber == 2:
        print("You picked scissors and the computer picked paper. You Win!")
        playerWins += 2
    if number == 3 and computerNumber == 1:
        print("You picked scissors and the computer picked rock. You Lose!")
        computerWins += 2

if playerWins > 0:
    print("You won. Game Over")
if computerWins > 0:
    print("The computer won. Game Over")