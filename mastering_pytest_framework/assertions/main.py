# Write pytest test functions below to validate the following:
# 1. Check that is_even(4) returns True.
# 2. Check that add(2, 3) equals 5.
# 3. Check that multiply(3, 7) returns 21 with a detailed message if it fails.
# 4. Check that divide(10, 0) raises a ZeroDivisionError.
# 5. Check that 'grape' is in the fruit_list.

def is_even(num):
    return num % 2 == 0

def add(a, b):
    return a + b

def multiply(a, b):
    return a * b

def divide(a, b):
    return a / b

fruit_list = ['apple', 'orange', 'grape', 'banana']

# Write your pytest test functions below. Name them as test_* following pytest convention.

def test_is_even():
    assert is_even(4)

def test_add():
    assert add(2, 3) == 5

def test_multiply():
    assert multiply(3,7), f"Expected 21, got {result}"

def test_divide_zero():
    try:
        divide(10,0) 
    except ZeroDivisionError:
        pass
    else:
        assert False, "Expected ZeroDivisionError when dividing by zero"

def test_grape_in_list():
    assert 'grape' in fruit_list

