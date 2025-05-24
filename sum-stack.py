def sum_using_stacks(num1, num2):
    stack1 = list(map(int, str(num1)))
    stack2 = list(map(int, str(num2)))
    
    result_stack = []
    carry = 0

    while stack1 or stack2 or carry:
        digit1 = stack1.pop() if stack1 else 0
        digit2 = stack2.pop() if stack2 else 0

        total = digit1 + digit2 + carry
        result_stack.append(total % 10)
        carry = total // 10

    result = ""
    while result_stack:
        result += str(result_stack.pop())

    return result


num1 = 789
num2 = 987
print(sum_using_stacks(num1, num2))