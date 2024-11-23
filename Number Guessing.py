import random

ranks = [
    "Iron 1", "Iron 2", "Iron 3",
    "Bronze 1", "Bronze 2", "Bronze 3",
    "Silver 1", "Silver 2", "Silver 3"
    "Gold 1", "Gold 2", "Gold 3",  # Gold ranks
    "Platinum 1", "Platinum 2", "Platinum 3",  # Platinum ranks
    "Diamond 1", "Diamond 2", "Diamond 3",  # Diamond ranks
    "Immortal 1", "Immortal 2", "Immortal 3",  # Immortal ranks
    "Radiant"  # Radiant
]

def number_guessing_game():
    # Initialize player's correct guess count and rank
    correct_guesses = 0
    current_rank = 0  # Starts at Iron 1

    # Display welcome message
    print("Welcome to the Number Guessing Game!")
    print("I have selected a number between 1 and 100.")
    print("Your task is to guess the number.")
    print("Every 5 correct guesses will increase your rank!")

    while True:
        # Generate a random number between 1 and 100
        random_number = random.randint(1, 100)
        attempts = 0  # Track the number of attempts for the current game

        while True:
            # Prompt the user for a guess
            user_guess = input("Enter your guess: ")

            # Validate the input to ensure it's a number
            if not user_guess.isdigit():
                print("Please enter a valid number.")
                continue

            # Convert the input to an integer
            user_guess = int(user_guess)

            # Increment the attempt count
            attempts += 1

            # Compare the user's guess to the random number
            if user_guess < random_number:
                print("Too low! Try again.")
            elif user_guess > random_number:
                print("Too high! Try again.")
            else:
                correct_guesses += 1
                print(f"Congratulations! You've guessed the correct number {random_number} in {attempts} attempts.")
                print(f"Your current rank is: {ranks[current_rank]}")

                # Check if the player has reached 5 correct guesses to rank up
                if correct_guesses % 5 == 0:
                    # Rank up after 5 correct guesses
                    if current_rank < len(ranks) - 1:
                        current_rank += 1  # Rank up
                        print(f"Congrats! You've ranked up to {ranks[current_rank]}!")
                    else:
                        print("You've reached the highest rank! Radiant!")
                break  # End the current guessing game

        # Optionally ask if the user wants to play again
        play_again = input("Do you want to play again? (yes/no): ").strip().lower()
        if play_again != "yes":
            print("Thanks for playing! Your final rank is:", ranks[current_rank])
            break

# Run the game
number_guessing_game()
