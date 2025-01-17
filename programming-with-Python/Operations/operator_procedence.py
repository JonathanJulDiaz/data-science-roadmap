# Python operators have procedences

# The order of the procedence is:
# 1. Parentheses
print(2 + (3 * 4))
# 2. Exponentiation
print(2 ** 3)
# 3. Multiplication and division
print(2 * 3 / 4)
# 4. Addition and subtraction
print(2 + 3 - 4)

# Operators with higher precedence are evaluated first
# and lower precedence are evaluated last

# And operators with the same precedence are evaluated from left to right

# Try to guess the result of the following expression
print((2 + 3) * 4 ** 2 - 1)