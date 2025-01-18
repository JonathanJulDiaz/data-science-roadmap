# In this problem the user will enter a phone number
# and then we must print each number verbally from the phone number
# for example: the number 1234 will be printed as "one two three four"
# we can use a dictionary to do that

# Solution

phone_number = input("Enter a phone number: ")

digits = {
    "0": "Zero",
    "1": "One",
    "2": "Two",
    "3": "Three",
    "4": "Four",
    "5": "Five",
    "6": "Six",
    "7": "Seven",
    "8": "Eight",
    "9": "Nine"
}

output = ""

for digit in phone_number:
    output += digits.get(digit, "!") + " "

print(output)