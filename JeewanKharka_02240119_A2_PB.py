def pokemon_card_binder():
    """
    Pokemon Card Binder Manager:
    Simulates organizing Pokemon cards into a virtual binder with fixed slots.
    Each card is mapped by Pokedex number (1–1025) into a 3D binder layout:
      - 64 cards per page (8x8 grid),
      - Cards positioned by row and column.
    """

    binder = {}  # Dictionary to store cards with their positions
    max_pokedex = 1025  # Total number of Pokémon

    def get_position(pokedex_number):
        """
        Converts a Pokedex number to its position in the binder:
        - page = (index // 64) + 1 → 64 cards per page
        - row = ((index % 64) // 8) + 1 → 8 rows per page
        - col = (index % 8) + 1 → 8 columns per row
        """
        index = pokedex_number - 1
        page = index // 64 + 1
        row = (index % 64) // 8 + 1
        col = (index % 8) + 1
        return page, row, col

    def add_card():
        """
        Adds a new card to the binder:
        - Checks if it's a valid Pokedex number.
        - If card already exists, displays its location.
        - Otherwise, calculates position and stores it.
        - Alerts when the binder is fully completed (all 1025 cards).
        """
        try:
            number = int(input("Enter Pokedex number (1–1025): "))
            if number < 1 or number > max_pokedex:
                print("Invalid Pokedex number.")
                return

            if number in binder:
                page, row, col = binder[number]
                print(f"Page: {page}")
                print(f"Position: Row {row}, Column {col}")
                print(f"Status: Pokedex #{number} already exists in binder.")
            else:
                page, row, col = get_position(number)
                binder[number] = (page, row, col)
                print(f"Page: {page}")
                print(f"Position: Row {row}, Column {col}")
                print(f"Status: Added Pokedex #{number} to binder")
                if len(binder) == max_pokedex:
                    print("You have caught them all!!")  # Completion alert
        except ValueError:
            print("Invalid input. Please enter a valid number.")

    def reset_binder():
        """
        Clears the binder after confirmation from the user.
        Prevents accidental data loss by requiring 'CONFIRM'.
        """
        print("WARNING: This will delete ALL Pokemon cards from the binder.")
        print("This action cannot be undone.")
        choice = input("Type 'CONFIRM' to reset or 'EXIT' to return to the Main Menu: ")
        if choice == "CONFIRM":
            binder.clear()
            print("The binder reset was successful! All cards have been removed.")
        else:
            print("Reset cancelled.")

    def view_binder():
        player_scores = {"pokemon": 0, "total": 0}  # Initialize as a dictionary
        """
        Displays the current contents of the binder:
        - Lists all stored Pokémon with their page and position.
        - Shows total cards and percentage completion.
        """
        print("Current Binder Contents:")
        print("------------------------")
        if not binder:
            print("The binder is empty.")
        else:
            for number in sorted(binder):
                page, row, col = binder[number]
                print(f"Pokedex #{number}:\nPage: {page}\nPosition: Row {row}, Column {col}")
        print("------------------------")
        total = len(binder)
        percent = round(total / max_pokedex * 100, 1)
        print(f"Total cards in binder: {total}")
        print(f"% completion: {percent}%")

        # Update scores
        player_scores["pokemon"] = int(percent)  # Store as whole number
        player_scores["total"] = sum(player_scores.values())

    # Main loop for binder manager
    while True:
        print("\nWelcome to Pokemon Card Binder Manager!")
        print("Main Menu:")
        print("1. Add Pokemon card")
        print("2. Reset binder")
        print("3. View current placements")
        print("4. Exit")
        choice = input("Select option: ")
        if choice == "1":
            add_card()
        elif choice == "2":
            reset_binder()
        elif choice == "3":
            view_binder()
        elif choice == "4":
            print("Thank you for using Pokemon Card Binder Manager!")
            break
        else:
            print("Invalid choice. Try again.")

# Call the function to start the program
pokemon_card_binder()
