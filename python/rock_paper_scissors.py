import random

def play_game():
    choices = ["rock", "paper", "scissors"]
    user_score = 0
    computer_score = 0

    while True:
        print("\nYour choices are:")
        for i, choice in enumerate(choices, 1):
            print(f"{i}. {choice.capitalize()}")

        user_choice = input("Enter your choice (1, 2, 3 or 'quit' to stop): ").lower()
        if user_choice == 'quit':
            print("\nFinal Scores:")
            print(f"You: {user_score}, Computer: {computer_score}")
            print("Thanks for playing!")
            break

        if user_choice not in ["1", "2", "3"]:
            print("Invalid choice. Please try again.")
            continue

        user_choice = choices[int(user_choice) - 1]
        computer_choice = random.choice(choices)

        print(f"\nYou chose: {user_choice.capitalize()}")
        print(f"Computer chose: {computer_choice.capitalize()}")

        if user_choice == computer_choice:
            print("It's a tie!")
        elif (user_choice == "rock" and computer_choice == "scissors") or \
             (user_choice == "paper" and computer_choice == "rock") or \
             (user_choice == "scissors" and computer_choice == "paper"):
            print("You win!")
            user_score += 1
        else:
            print("Computer wins!")
            computer_score += 1

if __name__ == "__main__":
    play_game()
