# return statement - returns a value from a function

# 7 + 8 - 4

def add(num1, num2):
    pass
    sum = num1 + num2
    return sum

def subtract(num1, num2):
    difference = num1 - num2
    return difference

partial_calculated_value = add(7, 8)
final_result = subtract(partial_calculated_value, 4)

print(final_result)