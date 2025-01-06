
def calculate_product_and_addition(num1, num2):
    product = num1 * num2
    add = product + num2
    return add


def calculate_sum_and_result(num1, num2):
    sum = num1 + num2  
    result = calculate_product_and_addition(num1, num2)  
    return sum, result

num1 = 5
num2 = 3
sum_result, complex_result = calculate_sum_and_result(num1, num2)
print(f"Sum of {num1} and {num2}: {sum_result}")
print(f"Complex result: {complex_result}")