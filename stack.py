def evaluate(expression):
    stack = []

    if " " in expression:
        tokens = expression.split()
    else:
        tokens = list(expression)

    for symbol in tokens:
        if symbol.lstrip('-').isdigit():
            stack.append(int(symbol))
        else:
            if len(stack) < 2:
                return "Error: Not enough operands"

            b = stack.pop()
            a = stack.pop()

            if symbol == '+':
                result = a + b
            elif symbol == '-':
                result = a - b
            elif symbol == '*':
                result = a * b
            elif symbol == '/':
                if b == 0:
                    return "Error: Division by zero"
                result = int(a / b)
            else:
                return f"Error: Unknown operator {symbol}"

            stack.append(result)

    return stack.pop() if len(stack) == 1 else "Error: Invalid expression"

exps = input("Enter postfix expression (with or without spaces): ")
print(evaluate(exps))
