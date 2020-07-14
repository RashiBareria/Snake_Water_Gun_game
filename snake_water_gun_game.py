#Snake_water_gun_game

import random

try:

    global num_of_chance_left
    num_of_chance_left = 10
    global score
    score = 0

    print("Developer: Rashi Bareria.  Welcome to Snake Water Gun game!\n")
    print("Game instruction: This is a Two Player game where each player chooses one object from the choice - Snake, Water, Gun. Second Player is computer\n")
    print("Rules: \n\t1. Snake vs. Water: Snake drinks the water hence wins. \n\t2. Water vs. Gun: The gun will drown in water, hence a point for water \n\t3. Gun vs. Snake: Gun will kill the snake and win.\n\tIn situations where both players choose the same object, the result will be a draw.\n\n There are 10 chances to win. Winner will be announced after calculating points\n")

    player_name=input("Enter player name: ")

    while(num_of_chance_left!=0):

        player_choice=int(input("\nPress 1 to select Snake\nPress 2 to select Water\nPress 3 to select Gun\n"))

        choice_list=["Snake", "Water", "Gun"]
        winning_choice = random.choice(choice_list)

        if player_choice==1: # 1 is for chosing snake
            if winning_choice=="Snake":
                print("*** Draw! Try again ***")
                print(f"Player's choice- Player 1: Snake    Player 2: {winning_choice}")
                num_of_chance_left-=1
                print(f"Number of chances left = {num_of_chance_left}")
                print("____________________")
            elif winning_choice == "Water":
                print("*** You Won! You are rewarded with 1 point ***")
                print(f"Player's choice- Player 1: Snake    Player 2: {winning_choice}")
                num_of_chance_left -= 1
                print(f"Number of chances left = {num_of_chance_left}")
                print("____________________")
                score+=1
            elif winning_choice == "Gun":
                print("*** You lose! Try again ***")
                print(f"Player's choice- Player 1: Snake    Player 2: {winning_choice}")
                num_of_chance_left -= 1
                print(f"Number of chances left = {num_of_chance_left}")
                print("____________________")
            else:
                print("Invalid Input! Choose from the above only.")
                print("____________________")
        elif player_choice==2: # 2 is for chosing water
            if winning_choice=="Snake":
                print("*** You lose! Try again ***")
                print(f"Player's choice- Player 1: Water    Player 2: {winning_choice}")
                num_of_chance_left -= 1
                print(f"Number of chances left = {num_of_chance_left}")
                print("____________________")
            elif winning_choice=="Water":
                print("*** Draw! Try again ***")
                print(f"Player's choice- Player 1: Water    Player 2: {winning_choice}")
                num_of_chance_left -= 1
                print(f"Number of chances left = {num_of_chance_left}")
                print("____________________")
            elif winning_choice=="Gun":
                print("*** You Won! You are rewarded with 1 point ***")
                print(f"Player's choice- Player 1: Water    Player 2: {winning_choice}")
                num_of_chance_left -= 1
                print(f"Number of chances left = {num_of_chance_left}")
                print("____________________")
            else:
                print("Invalid Input! Choose from the above only.")
        elif player_choice==3: # 3 is for chosing gun
            if winning_choice=="Snake":
                print("*** You Won! You are rewarded with 1 point ***")
                print(f"Player's choice- Player 1: Gun    Player 2: {winning_choice}")
                num_of_chance_left -= 1
                print(f"Number of chances left = {num_of_chance_left}")
                print("____________________")
            elif winning_choice=="Water":
                print("*** You lose! Try again ***")
                print(f"Player's choice- Player 1: Gun    Player 2: {winning_choice}")
                num_of_chance_left -= 1
                print(f"Number of chances left = {num_of_chance_left}")
                print("____________________")
            elif winning_choice=="Gun":
                print("*** Draw! Try again ***")
                print(f"Player's choice- Player 1: Gun    Player 2: {winning_choice}")
                num_of_chance_left -= 1
                print(f"Number of chances left = {num_of_chance_left}")
                print("____________________")
            else:
                print("Invalid Input! Choose from the above only.")
        else:
            print("Invalid Input! Choose from the above only.")

    if num_of_chance_left==0:
        print(f"Game over! \n\n{player_name}'s Score = {score}")

except Exception as e:
    print("Something went wrong! Run the game again.")





