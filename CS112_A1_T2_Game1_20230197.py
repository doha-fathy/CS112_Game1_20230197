#File name: CS112_A1_T2_Game1_20230197.py

# Purpose: 100 game is game for two players to take turn starting
#          of zero alternatively each adding a number from 1 to 10
#          to the sum  the first player who reaches 100 wins.

# Author: Doha Fathy Refaey Khodary Mustafa
# ID: 20230197

# welcome message
print("welcome to 100 game")
print("player 1 will play first")

sum = 0  # game date

# game playing
while True:
    try:
        player1_number = int(input("player 1 number : "))

        # validation of player1_number
        while (player1_number < 1) or (player1_number > 10):
            print("player 1 please enter number from 1 to 10")
            player1_number = int(input("player 1 number : "))

        sum = sum + player1_number

        # validation if player1_number makes sum greater than 100
        while sum > 100:
            sum = sum - player1_number
            print("player 1 please enter number in range 1 to ", 100 - sum)
            player1_number = int(input("player 1 number : "))
            sum = sum + player1_number

        print("sum = ", sum)

        # check about sum
        if sum == 100:
            print("player 1 won")
            break

        player2_number = int(input("player 2 number : "))

        # validation of player2_number
        while (player2_number < 1) or (player2_number > 10):
            print("player 2 please enter number from 1 to 10")
            player2_number = int(input("player 2 number : "))
        sum = sum + player2_number

        # validation if player2_number makes sum greater than 100
        while sum > 100:
            sum = sum - player2_number
            print("player 2 please enter number in range 1 to ", 100 - sum)
            player2_number = int(input("player 2 number : "))
            sum = sum + player2_number

        print("sum = ", sum)

        # check about sum
        if sum == 100:
            print("player 2 won")
            break

    except:
        print("Please enter a valid number")