import random

def generate_array():
    """
    generate_array(): Creates and returns an array of 10,000 evenly distributed 0's and 1's.
    """
    arr = []
    for i in range(0, 10_000):
        arr.append(random.randint(0,1))
    return arr

def find_one(arr, k):
    """
    find_one(): Searches a random index between 0 and 10,000. If 1 is the value the index is returned.
    Stops if one is not found after k tries.
    Parameters: A random array of 0's and 1's and number of attempts (k).
    """
    k_count = 0
    while True:
        k_count += 1
        idx = random.randint(0,10_000)
        if arr[idx] == 1:
            print(f"1 was found at index {idx} after {k_count} tries.")
            break
        elif arr[idx] != 1:
            k -= 1
            if k == 0:
                print(f"Program timed out. Could not locate 1 after {k_count} tries.")
                break

def main():
    """
    main(): Continuously asks for k then uses that and generate_array() as arguments for find_one().
    """
    while True:
        try:
            k = int(input("Please enter a limit for the Monte Carlo algorithm: "))
        except:
            print("Please enter a positive integer.")
        arr = generate_array()
        find_one(arr, k)
        
main()