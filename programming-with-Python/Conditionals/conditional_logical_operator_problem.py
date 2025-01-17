# Considering the conditions on conditions_2.txt
# we will simulate this rules using Python

# First we must initialize the boolean variables high_income and good_credit
has_high_income = True
has_good_credit = True

# Now we have to use the conditional if, which is used to execute a block of code indenteded after it
# if the boolean variable next to it is true
if has_high_income and has_good_credit:
    print("Eligible for loan")