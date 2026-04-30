import random

die_faces = [1, 2, 3, 4, 5, 6]
random.shuffle(die_faces)

# Step 1: Create an iterator from the shuffled list
die_iterator = iter(die_faces)

# Step 2: Roll the die using `next()`
try:
    while True:
        face =  next(die_iterator)
        print(f"Rolled: {face}")
except StopIteration:
    print("All rolls complete.")