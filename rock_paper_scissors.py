import random
print("...rock...")
print("...paper...")
print("...scissors...")

player_name = input("What is your name? \n")

def start():

	play = True

	while play:

		game_type = input("Would you like to play best of or first to? (best/first)\n").lower()
		computer_wins = 0
		player_wins = 0
		games_played = 0

		while game_type != "best" and game_type != "first":
			print("Oops, you didn't enter a valid gamemode.")
			game_type = input("Would you like to play best of or first to? (best/first)\n").lower()

		if game_type == "best":
			
			best_of = int(input("What would you like to play best of? (3/5)\n"))

			while best_of != 3 and best_of != 5:
				print("Oops, you didn't enter a valid amount. Please try again")
				best_of = int(input("What would you like to play best of? (3/5)\n"))

			else:
				while games_played < best_of:
					player_move = input(player_name + ", make your move: \n").lower()
					rand_num = random.randint(0,2)

					if rand_num == 0:
						computer_move = "rock"
				
					elif rand_num == 1:
						computer_move = "paper"
				
					else:
						computer_move = "scissors"

					while player_move not in ['rock', 'scissors', 'paper']:
						print("Please enter a valid move.")
						player_move = input(player_name + ", make your move: \n").lower()

					else:
						print(f"Computer plays {computer_move}")

						if player_move == computer_move:
							print("It's a tie!")
							games_played += 1
							best_of += 1
							print(str(player_wins) + " : " + str(computer_wins))
							
						elif player_move == "rock":
							if computer_move == "scissors":
								print(player_name + " wins!")
								player_wins = player_wins + 1
								games_played += 1
								print(str(player_wins) + " : " + str(computer_wins))
							elif computer_move == "paper":
								print("The computer wins!")
								computer_wins = computer_wins + 1
								games_played += 1
								print(str(player_wins) + " : " + str(computer_wins))

						elif player_move == "paper":
							if computer_move == "rock":
								print(player_name + " wins!")
								player_wins = player_wins + 1
								games_played += 1
								print(str(player_wins) + " : " + str(computer_wins))
							elif computer_move == "scissors":
								print("The computer wins!")
								computer_wins = computer_wins + 1
								games_played += 1
								print(str(player_wins) + " : " + str(computer_wins))

						elif player_move == "scissors":
							if computer_move == "paper":
								print(player_name + " wins!")
								player_wins = player_wins + 1
								games_played += 1
								print(str(player_wins) + " : " + str(computer_wins))
							elif computer_move == "rock":
								print("The computer wins!")
								computer_wins = computer_wins + 1
								games_played += 1
								print(str(player_wins) + " : " + str(computer_wins)) 

				play = False
				break	

		if game_type == "first":
			first_to = int(input("What would you like to play first to? (1/2/3/4/5)\n"))

			while first_to not in [1,2,3,4,5]:
				print("Oops, you didn't enter a valid amount. Please try again")
				first_to = int(input("What would you like to play first to? (1/2/3/4/5)\n"))

			else:

				while player_wins < first_to and computer_wins < first_to:
					player_move = input(player_name + ", make your move: \n").lower()
					rand_num = random.randint(0,2)

					if rand_num == 0:
						computer_move = "rock"
				
					elif rand_num == 1:
						computer_move = "paper"
				
					else:
						computer_move = "scissors"

					while player_move not in ['rock', 'scissors', 'paper']:
						print("Please enter a valid move.")
						player_move = input(player_name + ", make your move: \n").lower()

					else:
						print(f"Computer plays {computer_move}")

						if player_move == computer_move:
							print("It's a tie!")
							print(str(player_wins) + " : " + str(computer_wins))
							
						elif player_move == "rock":
							if computer_move == "scissors":
								print(player_name + " wins!")
								player_wins = player_wins + 1
								print(str(player_wins) + " : " + str(computer_wins))
							elif computer_move == "paper":
								print("The computer wins!")
								computer_wins = computer_wins + 1
								print(str(player_wins) + " : " + str(computer_wins))

						elif player_move == "paper":
							if computer_move == "rock":
								print(player_name + " wins!")
								player_wins = player_wins + 1
								print(str(player_wins) + " : " + str(computer_wins))
							elif computer_move == "scissors":
								print("The computer wins!")
								computer_wins = computer_wins + 1
								print(str(player_wins) + " : " + str(computer_wins))

						elif player_move == "scissors":
							if computer_move == "paper":
								print(player_name + " wins!")
								player_wins = player_wins + 1
								print(str(player_wins) + " : " + str(computer_wins))
							elif computer_move == "rock":
								print("The computer wins!")
								computer_wins = computer_wins + 1
								print(str(player_wins) + " : " + str(computer_wins)) 

				play = False
				break	

	if computer_wins > player_wins:
		print("The computer beat you by a score of " + str(computer_wins) + " : " + str(player_wins))
	if player_wins > computer_wins:
		print("You beat the computer by a score of " + str(player_wins) + " : " + str(computer_wins))
	
	play_again = input("Do you want to play again? (y/n) ")

	if play_again == 'y':
		start()
	else:
		print("Thanks for playing!")

start()



