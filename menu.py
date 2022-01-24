# Catherine McLellan
# Menu
# Computer Science 30
# January 24, 2022

import chain_rule

# Printing menu for the user to use
print("Derivative Calculator")
print("")
menu = ("1. Chain-rule",
        "2. How to enter equations in this program", "3. Quit")
while True:
    for options in menu:
        print(options)
    selected_option = input("What do you need help with?")
    # Imported function from chain_rule file to calculate
    # the derivative of the user's function
    if selected_option == "1":
        try:
            chain_rule.simplify_derivative()
        except ValueError:
            print("""This equation is not recognized!
If you are unsure of how to type in your equation, press 2.""")
    # If the user wishes to learn about how to enter an
    # equation that will work with this program.
    elif selected_option == "2":
        instructions = open("equation_instructions.txt")
        for line in instructions:
            print(line)
    # Option to quit the program.
    elif selected_option == "3":
        print("Thank you for using this program!")
        break
    # If player enters something invalid.
    else:
        print("Please enter a number on the menu.")
