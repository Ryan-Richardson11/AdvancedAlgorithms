import random

def generate_array():
    """
    generate_array(): Creates and returns an array of 10,000 evenly distributed 0's and 1's.
    """
    arr = []
    for i in range(0, 10_000):
        arr.append(random.randint(0,1))
    return arr

def find_one(arr):
    """
    find_one(): Searches a random index between 0 and 10,000. If 1 is the value the index is returned.
    Parameters: A random array of 0's and 1's.
    """
    count = 0
    while True:
        idx = random.randint(0,10_000)
        count += 1
        if arr[idx] == 1:
            print(f"1 was found at index {idx} after {count} tries")
            break

def main():
    """
    main(): Continuously asks for k then uses that and generate_array() as arguments for find_one().
    """
    arr = generate_array()
    find_one(arr)

main()