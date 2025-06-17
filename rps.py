

import random
import emoji

def get_emoji(choice):
    if choice == 0:
        return emoji.emojize(":oncoming_fist:")  # Rock
    elif choice == 1:
        return emoji.emojize(":raised_hand:")    # Paper
    elif choice == 2:
        return emoji.emojize(":victory_hand:")   # Scissors

def print_emoji(user_choice, computer_choice):
    print(f"User choice: {get_emoji(user_choice)}  Computer choice: {get_emoji(computer_choice)}")

def rps():
    round = int(input("How many rounds do you want? "))
    count = 1
    user_score = 0
    comp_score = 0

    while count <= round:
        print(f"\nRound {count}")
        try:
            user_choice = int(input("Enter your choice: 0 for rock, 1 for paper, 2 for scissors\n"))
            if user_choice not in [0, 1, 2]:
                print("Invalid choice. Try again.")
                continue
        except ValueError:
            print("Please enter a valid number.")
            continue

        computer_choice = random.randint(0, 2)
        print_emoji(user_choice, computer_choice)

        # Determine winner
        if user_choice == computer_choice:
            print("It's a draw!")
        elif (user_choice == 0 and computer_choice == 2) or \
             (user_choice == 1 and computer_choice == 0) or \
             (user_choice == 2 and computer_choice == 1):
            print("You win this round!")
            user_score += 1
        else:
            print("Computer wins this round!")
            comp_score += 1

        count += 1

    # Final Result
    print("\nFinal Score:")
    print(f"You: {user_score} | Computer: {comp_score}")
    if user_score == comp_score:
        print("It's a tie!")
    elif user_score > comp_score:
        print("🎉 You won the game!")
    else:
        print("😢 Computer won the game.")

def main():
    rps()

if __name__ == "__main__":
    main()



