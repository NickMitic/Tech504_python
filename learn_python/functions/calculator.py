import re

def add(num1, num2):
    return str(float(num1) + float(num2))

def subtract(num1, num2):
    return str(float(num1) - float(num2))

def multiply(num1, num2):
    return str(float(num1) * float(num2))

def divide(num1, num2):
    return str(float(num1) / float(num2))

def exponentiate(num, power):
    return str(float(num) ** float(power))

def find_inner_brackets(string):
    return re.findall(r"\([^()]*\)", string)

def expression_list(string):
    terms = re.split(r"([+\-*/^])", string)
    negative_number_at = []
    for i in range(len(terms)):
        if terms[i] == "-" and terms[i-1] == "":
            negative_number_at.append(i)
    if negative_number_at:
        for i in range(len(negative_number_at)):
            terms[negative_number_at[i] - 1 - (2 * i):negative_number_at[i] + 2 - (2 * i)] = ["".join(terms[negative_number_at[i] - 1 - (2 * i):negative_number_at[i] + 2 - (2 * i)])]
    return terms

def podmas(string):
    string = string.replace("(", "").replace(")", "")
    terms = expression_list(string)
    for i in range(len(terms)):
        if terms[i] == "^":
            string = string.replace(terms[i - 1] + "^" + terms[i + 1],exponentiate(terms[i - 1],terms[i + 1]))
    terms = expression_list(string)
    for i in range(len(terms)):
        if terms[i] == "/":
            string = string.replace(terms[i - 1] + "/" + terms[i + 1],divide(terms[i - 1],terms[i + 1]))
    while "*" in string:
        terms = expression_list(string)
        for i in range(len(terms)):
            if terms[i] == "*":
                string = string.replace(terms[i - 1] + "*" + terms[i + 1],multiply(terms[i - 1],terms[i + 1]))
                break
    if "+" or "-" in string:
        terms = expression_list(string)
        for i in range(len(terms)):
            if terms[i] == "-":
                terms[i] = "+"
                terms[i + 1] = "-" + terms[i + 1]
        return str(sum([float(term) for term in terms if term != "+"]))
    else:
        return string


def evaluate_brackets(string):
    while "(" in string:
        inner_brackets = find_inner_brackets(string)
        for bracket in inner_brackets:
            string = string.replace(bracket,podmas(bracket))
    return string

def evaluate_expression(string):
    string = string.replace(" ", "")
    string = evaluate_brackets(string)
    string = podmas(string)
    return string

print(evaluate_expression("2*3*3") == "18.0")
print(evaluate_expression("((-1*4)/2)+(2^-1 +56)") == "54.5")
print(evaluate_expression("(((3-1)^2+3)/2)") == "3.5")
print(evaluate_expression("(4 / 2)^2 -((2*3)-(1+1)+12)/2") == "-4.0")





