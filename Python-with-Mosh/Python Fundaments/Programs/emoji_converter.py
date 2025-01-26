# Now we're going to create a emoji converter, which will convert text to emojis
# We will use a dictionary to store the emojis
emojis = {
    ":)" : "😀",
    ":(" : "😢",
    ":D" : "😀",
    ":P" : "😛",
    ":O" : "😲",
    ":(" : "😢"
}

# Now we will ask the user to enter some message
message = input("> ")

# Let's create a output message
output = ""

# Now we will loop through the message and replace the emojis
for word in message.split(" "):
        output += emojis.get(word, word) + " "


print(output)