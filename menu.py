import chain_rule

print("Derivative Calculator")
print("")
menu = ("1. Chain-rule",
        "2. How to enter equations in this program", "3. Quit")
while True:
    for options in menu:
        print(options)
    selected_option = input("What do you need help with?")
    if selected_option == "1":
        try:
            chain_rule.simplify_derivative()
        except ValueError:
            print("""This equation is not recognized!
If you are unsure of how to type in your equation, press 2.""")
    elif selected_option == "2":
        instructions = open("equation_instructions.txt")
        for line in instructions:
            print(line)
    elif selected_option == "3":
        print("Thank you for using this program!")
        break
    else:
        print("Please enter a number on the menu.")
