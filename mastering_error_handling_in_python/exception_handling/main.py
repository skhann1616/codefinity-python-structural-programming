def process_data(data):
    if not data:
        raise ValueError("Data list cannot be empty.")
    try:
        result = data[0] / data[-1]
    except ZeroDivisionError:
        print("Cannot divide by zero in the data.")
    except TypeError:
        print("Data should contain only numbers.")
    except IndexError:
        print("Data list is too short.")
    else:
        print(f"Result: {result}")
    finally:
        print("Data processing attempted.")

# Example usage
result = process_data([1, 2, 0])