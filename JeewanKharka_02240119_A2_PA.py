import random

# Dictionary to track player scores for all games
player_scores = {
    "number_guessing": 0,
    "rock_paper_scissors": 0,
    "quiz": 0,
    "pokemon": 0,
    "total": 0
}

def number_guessing_game():
    """
    Number Guessing Game:
    - Random number between 1 to 100 is generated.
    - User repeatedly inputs guesses.
    - Feedback is given: too low, too high, or correct.
    - Score increases by 10 per correct guess.
    - Loop continues until the player chooses to stop.
    """
    score = 0
    while True:
        number = random.randint(1, 100)
        attempts = 0
        guessed = False
        
        while not guessed:
            guess = int(input("Enter a number in the range of 1 and 100: "))
            attempts += 1
            
            if guess < number:
                print("Your guess is low, try again with higher values.")
            elif guess > number:
                print("Too high, try again with lower values.")
            else:
                print("Congratulations! You guessed the number.")
                score += 10
                guessed = True

        print(f"Your score: {score}")
        player_scores["number_guessing"] = score
        player_scores["total"] = sum(player_scores.values())
        
        play_again = input("Do you want to play the number guessing game again? (yes/no): ").lower()
        if play_again != "yes":
            print("Thanks for playing! Goodbye!")
            break

def Rock_Paper_Scissor():
    """
    Rock Paper Scissors Game:
    - Computer randomly selects rock/paper/scissors.
    - Player inputs their choice.
    - Game decides winner using standard rules:
        Rock > Scissors, Scissors > Paper, Paper > Rock.
    - Score: +10 for win, +5 for tie.
    """
    score = 0
    while True:
        computer_choice = random.choice(["rock", "paper", "scissors"])
        user_choice = input("Enter your choice (rock, paper, scissors): ").lower()
        if user_choice not in ["rock", "paper", "scissors"]:
            print("Invalid choice. Please choose rock, paper, or scissors.")
        else:
            print(f"Computer chose: {computer_choice}")
            if user_choice == computer_choice:
                print("It's a tie!")
                score += 5
            elif (user_choice == "rock" and computer_choice == "scissors") or \
                 (user_choice == "paper" and computer_choice == "rock") or \
                 (user_choice == "scissors" and computer_choice == "paper"):
                print("Dang, you win!")
                score += 10
            else:
                print("My bad, you lose!")

        print(f"Your score: {score}")
        player_scores["rock_paper_scissors"] = score
        player_scores["total"] = sum(player_scores.values())

        play_again = input("Do you want to attempt again? (yes/no): ").lower()
        if play_again == "no":
            print("Thanks for wasting your time!")
            break

def Multiple_Choice():
    """
    Multiple Choice Quiz:
    - 10 trivia questions with 4 options (A-D).
    - User selects their answer for each.
    - Immediate feedback is provided.
    - Final score is shown as percentage.
    - Tracks correct answers vs guesses.
    """
    questions = (
        "What is the x-axis called if you convert certain coordinates to polar coordinates?",
        "What did the photon say when it was asked if it needed to check a bag at the airport?",
        "Who is known as the father of history?",
        "Which is the first Dzong built by Zhabdrung in Bhutan and where is it located?",
        "Who was the first person to introduce Taekwondo to Bhutan?",
        "Which satellite was launched together with Bhutan-1, Bhutan's first satellite?",
        "What is the name of the traditional Bhutanese dance performed at the end of a special event to mark its successful conclusion?",
        "Who was the first education minister of Bhutan?",
        "The famous painting Mona Lisa was drawn by?",
        "The album 'CANT RUSH GREATNESS' is owned by?"
    )

    options = (
        ("A) Polar Axis", "B) X-Axis", "C) Initial line", "D) Z-Axis"),
        ("A) I don't know", "B) No thanks, I am travelling light", "C) I don't want to check", "D) I don't need to check"),
        ("A) Socrates", "B) Herodotus", "C) Aristotle", "D) Plato"),
        ("A) Punakha Dzong, Punakha", "B) Paro Dzong, Paro", "C) Simtokha Dzong, Thimphu", "D) Trongsa Dzong, Trongsa"),
        ("A) Grandmaster Yonten Tharchen", "B) Master Sonam Tobgay", "C) Dasho Jigme Thinley", "D) Coach Karma Tenzin"),
        ("A) CubeBel-1", "B) Maya-1", "C) UiTMSAT-1", "D) All of the above"),
        ("A) Shungcham Dance", "B) Chham", "C) Tashi Labey", "D) None in the list"),
        ("A) Lyonpo Thakur Singh", "B) Dasho Lyonpo Thakur", "C) Lyonpo Thakur Singh Powdyel", "D) Dasho Karma Ura"),
        ("A) Leonardo da Vinci", "B) Vincent van Gogh", "C) Pablo Picasso", "D) Claude Monet"),
        ("A) Jay-Z", "B) 2Pac", "C) IceCube", "D) Central Cee")
    )

    answers = ("A", "B", "B", "C", "A", "D", "B", "C", "A", "B")
    
    while True:
        guesses = []
        question_no = 0
        score = 0
        
        for question in questions:
            print("-------------------------------")
            print(question)
            for option in options[question_no]:
                print(option)

            guess = input("Enter A, B, C, D: ").upper()
            guesses.append(guess)
            if guess == answers[question_no]:
                print("Correct!")
                score += 1
            else:
                print("Incorrect!")
                print("The correct answer is " + answers[question_no])

            question_no += 1

        print("-----------------------------------------------------")
        print("                       RESULTS                       ")
        print("answers : ", " ".join(answers))
        print("guesses : ", " ".join(guesses))
        print(f"Total correct answers: {score} out of {len(questions)}")

        percent_score = int(score / len(questions) * 100)
        print(f"Your score is {percent_score}%")
        
        player_scores["quiz"] = percent_score
        player_scores["total"] = sum(player_scores.values())

        play_again = input("Do you want to play the quiz again? (yes/no): ").lower()
        if play_again != "yes":
            print("Thanks for playing! Goodbye!")
            break

def Overall_Scoring_System():
    """
    Displays scores from all games and the total.
    Useful for tracking performance across sessions.
    """
    print("\n--- Overall Scoring System ---")
    print("Number Guessing Game Score: " + str(player_scores["number_guessing"]))
    print("Rock Paper Scissors Score: " + str(player_scores["rock_paper_scissors"]))
    print("Quiz Score: " + str(player_scores["quiz"]))
    print("Pokemon Card Binder Score: " + str(player_scores["pokemon"]))
    print("Total Score: " + str(player_scores["total"]))
    input("Press Enter to continue...")

# Main Program Menu
while True:
    print("\nMenu:")
    print("1. Guess number game")
    print("2. Rock Paper Scissors game")
    print("3. Trivia pursuit quiz with different categories and multiple choices")
    print("4. Pokemon Card Binder Manager")
    print("5. Overall Scoring system")
    print("6. Exit")

    user_choice = int(input("Enter your choice: "))
    if user_choice == 6:
        print("Exited the program.")
        break
    elif user_choice == 1:
        number_guessing_game()
    elif user_choice == 2:
        Rock_Paper_Scissor()
    elif user_choice == 3:
        Multiple_Choice()
    elif user_choice == 5:
        Overall_Scoring_System()
    elif user_choice == 4:
        from Assignment_2_P2 import pokemon_card_binder
        pokemon_card_binder()
    else:
        print("Invalid choice. Try again.")
