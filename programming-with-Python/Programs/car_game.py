# We will create a car game, where the user can start the car, stop the car, or quit the game,
# and the user can type 'help' to see the available commands

# Ask the user what they want to do, to show the user that we wait for their input
# we will put '> ' in front of the input
command = input("> ").lower() # lower() is used to convert the input to lowercase, so it is not case sensitive

# We must write the code inside a loop, so that the user can continue to enter commands
while command != 'quit': # Condition to check if the user wants to quit the game

    if command == 'start':
        print("Car started... Ready to go")
    elif command == 'stop':
        print("Car stopped")
    elif command == 'help': # If the user enters 'help'
        print("""
        start - to start the car
        stop - to stop the car
        quit - to quit the game
        """)
    else: # If the user enters an invalid command
        print("Sorry, I don't understand that command")

    # And ask the user what they want to do again
    command = input("> ").lower()