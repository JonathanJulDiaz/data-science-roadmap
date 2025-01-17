# Let's make a guess the number game, where the user have certain numbers of tries
# to guess the number first we must initialize the number to guess
number_to_guess = 10

# To do that, we can use the loop while,
# because the while loop can have a else clause, which will be
# executed when the condition next to the while is false

tries = 0 # Variable to count the number of tries

while tries < 3: # Condition to check the number of tries
    guess = int(input("Guess the number: "))

    if guess == number_to_guess: # Condition to check if the guess is correct
        print("You win!")
        break # Here we break the loop because the user found the correct number
    else:
        print("Try again!")

    tries += 1 # Here we add 1 to the number of tries

else: # Else clause, which will be executed when the condition next to the while is false
    print("You lose!") # Here we print that the user lost