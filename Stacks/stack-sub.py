def dynamic_sub_using_stacks(num1, num2):
    str1, str2 = str(num1), str(num2)

    negative_result = False
    if int(str1) < int(str2):
        str1, str2 = str2, str1
        negative_result = True

    stack1 = list(map(int, str(str1)))
    stack2 = list(map(int, str(str2)))

    result_stack = []
    borrow = 0

    while stack1 or stack2:
        digit1 = stack1.pop() if stack1 else 0
        digit2 = stack2.pop() if stack2 else 0

        digit1 -= borrow

        if digit1 < digit2:
            digit1 += 10
            borrow = 1
        else:
            borrow = 0

        result_stack.append(digit1 - digit2)

    while len(result_stack) > 1 and result_stack[-1] == 0:
        result_stack.pop()

    result = ''
    while result_stack:
        result += str(result_stack.pop())

    return '-' + result if negative_result else result


# 🔥 Input section
num1 = int(input())
num2 = int(input())
print("Subtraction Result:", dynamic_sub_using_stacks(num1, num2))
