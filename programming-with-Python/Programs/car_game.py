# We will create a car game, where the user can start the car, stop the car, or quit the game,
# and the user can type 'help' to see the available commands

# Ask the user what they want to do, to show the user that we wait for their input
# we will put '> ' in front of the input
command = input("> ").lower() # lower() is used to convert the input to lowercase, so it is not case sensitive

is_car_started = False # Variable to check if the car is started

# We must write the code inside a loop, so that the user can continue to enter commands
while command != 'quit': # Condition to check if the user wants to quit the game

    if command == 'start':
        if is_car_started: # If the car is already started
            print("Car is already started")
        else:
            print("Car started... Ready to go")
            is_car_started = True
    elif command == 'stop' :
        if not is_car_started: # If the car is not started
            print("Car is already stopped")
        else:
            print("Car stopped")
            is_car_started = False
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