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
print("..rock")
print("..paper")
print("..scissors")

player1 = input("Player 1, make your move: ")
player2 = input("Player 2, make your move: ")

if player1 == player2:
	print("Its a tie!")
elif player1 == "rock":
	if player2 == "scissors":
		print("player1 wins!")
	elif player2 == "paper":
		print("player2 wins!")
elif player1 == "paper":
	if player2 == "rock":
		print("player1 wins")
	elif player2 == "scissors":
		print("player2 wins!")
elif player1 == "scissors":
	if player2 == "paper":
		print("player1 wins!")
	elif player2 == "rock":
		print("player2 wins!")
else:
	print("something went wrong")
