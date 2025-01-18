# Dictionaries in python can be useful to store data in key-value pairs
# They are also used to store data in a structured and dynamic way

customer = {
    "name": "John Doe",
    "age": 30,
    "is_verified": True
}

# In the dictionaries, we can use the keys to access the values
print(customer["name"]) # This will print John Doe

# We can also use the get() method
print(customer.get("name")) # This will print John Doe

# In case that the key doesn't exist, the get() method will return None
print(customer.get("birthdate")) # This will print None

# But if we want to get a default value if the key doesn't exist, we can use the get() method
print(customer.get("birthdate", "N/A")) # This will print N/A

# We can also change the value of a key
customer["name"] = "Jane Doe"
print(customer["name"]) # This will print Jane Doe

# Or create a new key
customer["birthdate"] = "01/01/1990"
print(customer["birthdate"]) # This will print 01/01/1990