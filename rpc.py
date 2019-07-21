#version 1

#if player1 == "rock" and player2 == "scissors":
#	print("player1 wins!")
#elif player1 == "rock" and player2 == "paper":
#	print("player2 wins!")
#elif player1 == "paper" and player2 == "rock":
#	print("player1 wins!")
#elif player1 == "paper" and player2 == "scissors":
#	print("player2 wins!")
#elif player1 == "scissors" and player2 == "rock":
#	print("player2 wins!")
#elif player1 == "scissors" and player2 == "paper":
#	print("player1 wins!")
#elif player1 == player2:
#	print("Its a tie!")
#else:
#	print("something went wrong")

#refactored 1

#if (player1 == "rock" and player2 == "scissors") or (player1 == "paper" and player2 == "rock") or (player1 == "scissors" and player2 == "paper"):
#	print("player1 wins!")
#elif (player1 == "rock" and player == "paper") or (player1 == "paper" and player2 == "scissors") or (player1 == "scissors" and player2 == "rock"):
#	print("player2 wins!")
#elif player1 == player2:
#	print("Its a tie!")
#else:
#	print("something went wrong")

# colt's more effiecient refactor 2 lol

#somethings wrong in terminal
# print("..rock")
# print("..paper")
# print("..scissors")

#player1 = input("Player 1, make your move: ")
#print("****NO CHEATING\n\n" * 20)
#player2 = input("Player 2, make your move: ")

#if player1 == player2:
#	print("Its a tie!")
#elif player1 == "rock":
#	if player2 == "scissors":
#		print("player1 wins!")
#	elif player2 == "paper":
#		print("player2 wins!")
#elif player1 == "paper":
#	if player2 == "rock":
#		print("player1 wins")
#	elif player2 == "scissors":
#		print("player2 wins!")
#elif player1 == "scissors":
#	if player2 == "paper":
#		print("player1 wins!")
#	elif player2 == "rock":
#		print("player2 wins!")
#else:
#	print("something went wrong")

#better shorter version

#if player1 == player2:
#	print("Draw")
#elif player1 == "rock" and player2 == "scissors":
#	print("player1 wins!")
#elif player1 == "paper" and player2 == "rock":
#	print("player1 wins!")
#elif player1 == "scissors" and player2 == "paper":
#	print("player1 wins!")
#else:
#	print("player2 wins!")

# AI version
from random import random

player = input("Player, make your move: ").lower()

rand_num = randint(0,2)
if rand_num == 0:
	computer = "rock"
elif rand_num == 1:
	computer = "paper"
else:
	computer = "scissors"
print(f"Computer playes {computer}")

if player == computer:
	print("Its a tie!")
elif player == "rock":
	if computer == "scissors":
		print("player wins!")
	# you can stay implicit or you can use else
	elif computer == "paper":
		print("computer wins!")
elif player == "paper":
	if computer == "rock":
		print("player wins!")
	elif computer == "scissors":
		print("computer wins!")
elif player == "scissors":
	if computer == "paper":
		print("player wins!")
	elif computer == "rock":
	 	print("computer wins!")
else:
	print("Enter a valid answer")