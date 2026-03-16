def divide_numbers(x, y):
    try:
        result = x / y
    except TypeError:
        print("Please enter only numbers.")
    except ZeroDivisionError:
        print("Cannot divide by zero.")
    else:
        print(f"The result is {result}")
    finally:
        print("Operation attempted.\n")

# Call the function to test the error handling
divide_numbers(6, 2)
divide_numbers(6, 0)
divide_numbers(6, 'o')