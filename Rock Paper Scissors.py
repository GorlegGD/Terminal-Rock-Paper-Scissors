import random


def Rock_Paper_Scissors():
    # Outer loop to handle restarting the entire game
    while True:
        choices = ['rock', 'paper', 'scissors']
        user_score = 0
        computer_score = 0
        total_rounds = 5
        current_round = 1

        print("\n" + "="*30)
        print(" NEW GAME STARTED ")
        print("="*30)
        print("Type 'exit' to end the game.")

        # Inner loop for the rounds
        while current_round <= total_rounds:
            print(f"\nRound {current_round}:")
            user_choice = input("Enter rock, paper, or scissors: ").lower()

            if user_choice == 'exit' or user_choice == 'quit':
                print("Exiting")
                return

            if user_choice not in choices:
                print("Invalid choice! Please try again.")
                continue

            computer_choice = random.choice(choices)
            print(f"Computer chose: {computer_choice}")

            if user_choice == computer_choice:
                print("It's a tie!")
            elif (user_choice == 'rock' and computer_choice == 'scissors') or \
                 (user_choice == 'paper' and computer_choice == 'rock') or \
                 (user_choice == 'scissors' and computer_choice == 'paper'):
                print("You win this round!")
                user_score += 1
            else:
                print("Computer wins this round!")
                computer_score += 1

            print(f"Scores -> You: {user_score}, Computer: {computer_score}")
            current_round += 1

        print(f"\nGame Over! Final Score -> You: {user_score}, Computer: {computer_score}")

        play_again = input("\nDo you want to play another game? (yes/no): ").lower()
        if play_again != 'yes' and play_again != 'y':
            print("Thanks for playing! Goodbye.")
        break


Rock_Paper_Scissors()
