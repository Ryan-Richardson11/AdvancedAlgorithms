import random

def generate_vector():
    """
    generate_vector(): 
    Creates an empty list then appends a random number from -100 to 100, 1000 times. The vector is then returned.
    """
    vector = []
    for i in range(0, 999):
        vector.append(random.randint(-100, 100))
    return vector