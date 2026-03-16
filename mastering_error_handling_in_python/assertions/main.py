# Existing function to add user details
def add_user(users, user_id, user_info):
    assert user_id not in users, "User ID already exists"
    assert isinstance(user_id, int), "User ID must be an integer"
    assert isinstance(user_info, dict), "User info must be a dictionary"

    users[user_id] = user_info
    print(f"Added user {user_id}")

# Test the function
users = {}
add_user(users, 1, {"name": "John", "age": 28})
add_user(users, 2, {"name": "Jane", "age": 32})
# The following will raise an assertion error
add_user(users, 1, {"name": "Alice", "age": 24})  # Duplicate user ID