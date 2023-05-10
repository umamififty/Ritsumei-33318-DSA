# Done by Khoo Zhenyu, 2600220458-3
# Done on April 27 2023
# This program converts a decimal number to binary using a stack.

def decimal_to_binary(decimal):
    stack = []
    binary = ''

    while decimal > 0:
        remainder = decimal % 2
        stack.append(remainder)
        decimal //= 2

    while stack:
        binary += str(stack.pop())

    return binary

input = int(input("Enter a number: "))
print(decimal_to_binary(input))