def calculate_product_and_addition(multiplier, addend):
    product = multiplier * addend
    result = product + addend
    return result


def calculate_sum_and_complex_result(num1, num2):
    total_sum = num1 + num2  # Compute the sum of the two numbers.
    complex_result = calculate_product_and_addition(num1, num2)  # Compute the complex result.
    return total_sum, complex_result



num1 = 5
num2 = 3
sum_result, complex_result = calculate_sum_and_complex_result(num1, num2)

print(f"Sum of {num1} and {num2}: {sum_result}")
print(f"Complex result: {complex_result}")
