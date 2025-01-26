# Now we're going to improve the emoji converter using a function

def emoji_converter(message):
    emojis = {
    ":)" : "😀",
    ":(" : "😢",
    ":D" : "😀",
    ":P" : "😛",
    ":O" : "😲",
    ":(" : "😢"
    }
    
    output = ""

    for word in message.split(" "):
        output += emojis.get(word, word) + " "
    return output
    


# Now we will ask the user to enter some message
message = input("> ")

# We call the function and print the return value
print(emoji_converter(message))