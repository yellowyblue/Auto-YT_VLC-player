# Function to perform arithmetic operations
def arithmetic_operations(a, b):
    sum_result = a + b
    difference_result = a - b
    product_result = a * b
    return sum_result, difference_result, product_result

# Main program
if __name__ == "__main__":
    # Input two integers
    num1 = int(input("Enter the first integer: "))
    num2 = int(input("Enter the second integer: "))

    # Perform arithmetic operations
    sum_result, difference_result, product_result = arithmetic_operations(num1, num2)

    # Output results
    print("Sum:", sum_result)
    print("Difference:", difference_result)
    print("Product:", product_result)
