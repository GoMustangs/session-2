import random

playerWins = 0
computerWins = 0

print("This is rock, paper, scissors. 1 = rock, 2 = paper, 3 = scissors. You will play against the computer to the best of 7 rounds.")

# game loop while neither the player or the computer has 4 wins
while playerWins < 4 and computerWins < 4:
    playerInput = input("Type in 1, 2, or 3: ")
    playerOutput = int(playerInput)
    computerOutput = random.randint(1,3)

    if playerOutput < 1 or playerOutput > 3:
        print("Invalid number.")

    if playerOutput == 1 and computerOutput == 1:
        print("You picked rock, and the computer picked rock. This round is a draw.")
    
    if playerOutput == 1 and computerOutput == 2:
        print("You picked rock, and the computer picked paper. The computer won this round.")
        computerWins+=1

    if playerOutput == 1 and computerOutput == 3:
        print("You picked rock, and the computer picked scissors. You won this round.")
        playerWins+=1
    
    if playerOutput == 2 and computerOutput == 1:
        print("You picked paper, and the computer picked rock. You won this round.")
        playerWins+=1
    
    if playerOutput == 2 and computerOutput == 2:
        print("You picked paper, and the computer picked paper. This round is a draw.")

    if playerOutput == 2 and computerOutput == 3:
        print("You picked paper, and the computer picked scissors. The computer won this round.")
        computerWins+=1
    
    if playerOutput == 3 and computerOutput == 1:
        print("You picked scissors, and the computer picked rock. The computer won this round.")
        computerWins+=1
    
    if playerOutput == 3 and computerOutput == 2:
        print("You picked scissors, and the computer picked paper. You won this round.")
        playerWins+=1

    if playerOutput == 3 and computerOutput == 3:
        print("You picked scissors, and the computer picked scissors. This round is a draw.")


# the end triggered when either the player or the computer has 4 wins
if playerWins == 4:
    print("You won the best of 7 games.")

if computerWins == 4:
    print("The computer won the best of 7 games.")