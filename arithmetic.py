# Function description: https://repl.it/github/freeCodeCamp/boilerplate-arithmetic-formatter

import re


def arithmetic_arranger(problems, print_result=False):

    first_line = ""
    second_line = ""
    dash_line = ""
    result_line = ""
    if len(problems) > 5:
        return "Error: Too many problems."

    for problem in problems:
        if "+" in problem:
            operator = "+"
        elif "-" in problem:
            operator = "-"
        else:
            return "Error: Operator must be '+' or '-'."

        numbers_str = problem.replace(" ", "").split(operator)

        if re.search("[^0-9]", numbers_str[0]) or re.search("[^0-9]", numbers_str[1]):
            return "Error: Numbers must only contain digits."

        # Only safe to turn strings to integers when numbers only contain digits
        numbers = [int(numbers_str[0]), int(numbers_str[1])]

        max_number = max(numbers[0], numbers[1])
        if max_number > 9999:
            return "Error: Numbers cannot be more than four digits."

        problem_width = len(str(max_number)) + 2

        first_line += (
            " " * (problem_width - len(numbers_str[0])) + numbers_str[0] + "    "
        )
        second_line += (
            operator
            + " " * (problem_width - len(numbers_str[1]) - 1)
            + numbers_str[1]
            + "    "
        )
        dash_line += "-" * problem_width + "    "
        result = (
            (numbers[0] + numbers[1]) if operator == "+" else (numbers[0] - numbers[1])
        )
        result_str = str(result)
        result_line += " " * (problem_width - len(result_str)) + result_str + "    "
    arranged_problems = "\n".join([first_line.rstrip(), second_line.rstrip(), dash_line.rstrip()]
    )
    if print_result:
        arranged_problems += "\n" + result_line.rstrip()
    return arranged_problems
