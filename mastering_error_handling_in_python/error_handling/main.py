def test_type_conversion():
    try:
        # Try to convert a string to an integer
        number = int("abc")
        print("Conversion result:", number)
    except ValueError:
        print("Handled ValueError: could not convert string to int.")

def test_list_access():
    try:
        # Try to access an invalid index in a list,
        # remember that the indexing of the elements starts from 0
        numbers = [1, 2, 3]
        print("Fourth element:", numbers[3])
    except IndexError:
        print("Handled IndexError: list index out of range.")

# Call functions to test error handling
test_type_conversion()
test_list_access()