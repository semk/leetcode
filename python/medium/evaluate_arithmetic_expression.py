#!/usr/bin/env python


def EvaluateExpression(exp):
    if not exp:
        return -1

    operands = []
    num = 0

    prevOperator = ''
    for char in exp:
        if char.isdigit():
            num = (num * 10) + int(char)
        else:
            operands.append(num)
            if prevOperator == '*':
                result = operands.pop() * operands.pop()
                operands.append(result)
            
            num = 0
            prevOperator = char

    if prevOperator == '*':
        result = operands.pop() * num
        operands.append(result)
    else:
        operands.append(num)

    return sum(operands)