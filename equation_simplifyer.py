import re
import time
new_function = ""
function_parts = []
symbol_reset = True
simp_powers = ""
pos_or_neg = "+"
coefficient = 1
power = 0
formula_terms = {}


class Terms:
    def __init__(self, name):
        self.name = name
        self.pos_or_neg = pos_or_neg
        self.coefficient = coefficient
        self.power = power


def split_function(formula):
    formula = re.split("\(|\)", formula)
    for parts in formula:
        if parts == "":
            formula.remove(parts)
    return formula


def bracket_powers(formula):
    counter = 0
    for parts in formula:
        if re.match("\^\d", parts):
            formula.remove(parts)
            power = int(parts.replace("^", ""))
            appender = formula[counter - 1]
            number = 1
            while power > number:
                formula.append(appender)
                number += 1
        counter += 1
    return formula


def multiply_terms(last_term, current_term):
    results = []
    for left_parts in last_term:
        for right_parts in current_term:
            results.append(left_parts + "*" + right_parts)
    return results


def resolve_pos_neg(term):
    sign = "-"
    neg = term.count("-")
    if neg % 2 == 0:
        sign = "+"
    term = re.sub("\+|\-", "", term)
    sign += term
    return sign


def foil_out_function(function):
    function_parts = []
    function = split_function(function)
    function = bracket_powers(function)
    for parts in function:
        parts = parts.replace(" ", "")
        parts = parts.replace("-", " -")
        parts = parts.replace("+", " +")
        function_parts += [parts.split(" ")]
    for terms in function_parts:
        for parts in terms:
            if parts == "":
                terms = terms.remove("")
    previous_term = "!!!"
    for terms in function_parts:
        if previous_term != "!!!":
            previous_term = multiply_terms(previous_term, terms)
        else:
            previous_term = terms
    strResult = ""
    for terms in previous_term:
        strResult += resolve_pos_neg(terms)
    return strResult


def simplify_powers(formula, variable):
    counter2 = 0
    pos_or_neg = "+"
    symbol_reset = True
    for terms in formula:
        if not symbol_reset:
            pos_or_neg = "+"
            symbol_reset = True
        if terms == "-":
            if pos_or_neg == "+":
                pos_or_neg = "-"
            elif pos_or_neg == "-":
                pos_or_neg = "+"
        if terms != "+" and terms != "-":
            symbol_reset = False
        terms = terms.split("*")
        counter = 0
        coefficient = 1
        power = 0
        if terms == [""]:
            continue
        elif (terms == ["+"] or terms == ["-"]):
            continue
        for parts in terms:
            parts = parts.split("^")
            if re.match(r'\d+{}'.format(variable), parts[0]):
                coefficient *= int(parts[0].replace("{}".format(variable), ""))
                power += 1
                if len(parts) > 1:
                    power -= 1
            elif re.match(r'\d+$', parts[0]) and variable == "x":
                coefficient *= int(parts[0])
            if parts == [variable]:
                power += 1
            try:
                if re.search(variable, parts[0]):
                    power += int(parts[1])
            except IndexError:
                continue
            counter += 1
        counter2 += 1
        name = 'term_{}'.format(counter2)
        pos_or_neg = "{}".format(pos_or_neg)
        power = "{}".format(power)
        coefficient = "{}".format(coefficient)
        if variable == "h":
            formula_terms[name].append([formula_terms.get(
                Terms(variable), variable),
                formula_terms.get(Terms(pos_or_neg), pos_or_neg),
                formula_terms.get(Terms(coefficient, ), coefficient),
                formula_terms.get(Terms(power), power)])
            continue
        formula_terms[name] = [[formula_terms.get(
            Terms(variable), variable),
            formula_terms.get(Terms(pos_or_neg), pos_or_neg),
            formula_terms.get(Terms(coefficient), coefficient),
            formula_terms.get(Terms(power), power)], ]
    return formula_terms


def separate_terms(formula):
    formula = re.sub("\*\*", "^", formula)
    formula = formula.replace(" ", "")
    formula = formula.replace("+", " + ")
    formula = formula.replace("-", " - ")
    formula = formula.split(" ")
    return formula


def append_to_function(function_terms, function):
    for terms in function_terms:
        counter = 0
        if (function_terms[terms][0][2] == "0" or
           function_terms[terms][1][2] == "0"):
            continue
        for parts in function_terms[terms]:
            if function_terms[terms][counter][0] == "h":
                function += "*{}{}**{}".format(
                    function_terms[terms][counter][2],
                    function_terms[terms][counter][0],
                    function_terms[terms][counter][3])
                continue
            function += " {}{}{}**{}".format(
                function_terms[terms][counter][1],
                function_terms[terms][counter][2],
                function_terms[terms][counter][0],
                function_terms[terms][counter][3])
            counter += 1
    return function


def powers_of_one(variable, function):
    function = function.split(" ")
    counter = 0
    newer_function = ""
    for terms in function:
        terms = re.sub('{}\*\*1'.format(variable), variable, terms)
        counter += 1
        newer_function += "{} ".format(terms)
    return newer_function


def powers_of_zero(variable, function):
    function = function.split(" ")
    counter = 0
    newer_function = ""
    for terms in function:
        terms = re.sub('{}\*\*0'.format(variable), '', terms)
        counter += 1
        newer_function += "{} ".format(terms)
    return newer_function


def times_one(function):
    function = re.sub("(?<=\D)[1](?=[xh])", "", function)
    function = re.sub("\*[1]\s|$(?=\D)", " ", function)
    return function


def common_terms(function):
    function = function.replace("+", " +")
    function = function.replace("-", " -")
    function = function.split(" ")
    powers = {}
    for terms in function:
        power = re.compile("\*\*\d")
        try:
            result = power.search(terms).group()
            power = result[2:]
            try:
                if powers[power]:
                    find = re.compile("[\+|\-]\dx")
                    coefficient1 = find.search(powers[power]).group()
                    coefficient1 = coefficient1[:-1]
                    coefficient2 = find.search(terms).group()
                    coefficient2 = coefficient2[:-1]
                    new_coefficient = eval(coefficient1 + coefficient2)
                    if new_coefficient > 0:
                        new_coefficient = "+" + str(new_coefficient)
                    if new_coefficient != 0:
                        powers[power] = str(
                                        new_coefficient) + "x**{}".format(
                                            power)
                    elif new_coefficient == 0:
                        powers[power] = ""
            except KeyError:
                powers[power] = terms
        except AttributeError:
            pass
    no_common_terms = ""
    for parts in powers:
        no_common_terms += powers[parts] + " "
    return no_common_terms


def simplify_function(function):
    function = foil_out_function(function)
    function_terms = separate_terms(function)
    formula_terms = simplify_powers(function_terms, "x")
    formula_terms = simplify_powers(function_terms, "h")
    newer_function = append_to_function(formula_terms, new_function)
    newer_function = powers_of_one("h", newer_function)
    newer_function = powers_of_zero("h", newer_function)
    newer_function = common_terms(newer_function)
    newer_function = powers_of_one("x", newer_function)
    newer_function = powers_of_zero("x", newer_function)
    newer_function = times_one(newer_function)
    if newer_function[0] == "+":
        newer_function = newer_function[1:]
    newer_function = newer_function.replace(" ", "")
    newer_function = newer_function.replace("+", " + ")
    newer_function = newer_function.replace("-", " - ")
    newer_function = newer_function.replace("**", "^")
    time.sleep(1)
    return newer_function
