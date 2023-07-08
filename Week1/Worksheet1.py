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

def MCSS(a):
    """
    MCSS(): 
    Initializes largest and accumulator to zero and itterates over inputted vector with a single for loop.
    Adds values to the accumulator and checks if acc > largest, if it is acc = largest.
    Skips if the start of iteration is negative and resets acc to zero.
    Returns the starting and ending indicies.
    """

    largest, acc, start, end, current = 0, 0, 0, 0, 0
    for j in range(len(a)):
        acc += a[j]
        if acc > largest:
            largest = acc
            start = current
            end = j
        if acc < 0:
            acc = 0
            current = j + 1
    return largest, f"Starting Index: {start} Ending Index: {end}"


def main():
    """
    Calls generate_vector() as v then passes it as an argument through MCSS and prints the sum.
    """
    v = generate_vector()
    print(v)
    max_sum = MCSS(v)
    print(f"The maximum contiguous subsequence sum is {max_sum}")

main()