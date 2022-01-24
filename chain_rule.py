# Catherine McLellan
# Computer Science 30
# January 24, 2022

import equation_simplifyer
import re
import time


def diff_eq():
    user_function = input("""Type your function.
f(x) = """)
    function = equation_simplifyer.simplify_function(user_function)
    if function == "1" and user_function != "1":
        raise ValueError
    elif function == "":
        raise ValueError
    print("Your foiled-out function is:")
    time.sleep(1)
    print(function)
    if "x" not in function:
        new_function = "0"
        return new_function
    new_function = ""
    if function[0] == "x":
        function = "1" + function
    function = function.replace(" ", "")
    function = function.replace("+", " +")
    function = function.replace("-", " -")
    function = function.split(" ")
    for terms in function:
        if terms == "x":
            terms = "1x"
        power = re.compile("\^\d")
        try:
            result = power.search(terms).group()
            power = result[1:]
        except AttributeError:
            if "x" in terms:
                power = "1"
            else:
                power = "0"
        coefficient = re.compile("\dx")
        try:
            result = coefficient.search(terms).group()
            coefficient = result[:-1]
        except AttributeError:
            coefficient = terms[1:]
        coefficient = int(coefficient) * int(power)
        if coefficient >= 0:
            coefficient = "+" + str(coefficient)
        power = int(power) - 1
        if coefficient != "+0":
            new_function += str(coefficient) + "x**{}".format(power)
    return new_function


def simplify_derivative():
    derivative = diff_eq()
    derivative = equation_simplifyer.powers_of_one("x", derivative)
    derivative = equation_simplifyer.powers_of_zero("x", derivative)
    if derivative[0] == "+":
        derivative = derivative[1:]
    time.sleep(1)
    print("Calculating derivative using chain-rule...")
    time.sleep(1)
    derivative = derivative.replace("**", "^")
    derivative = derivative.replace("+", " + ")
    derivative = derivative.replace("-", " - ")
    print(derivative)
