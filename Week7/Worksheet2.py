import random

def generate_array():
    arr = []
    for i in range(10_000):
        arr.append(random.randint(0,1))
    return arr

def find_one(arr, k):
    while True:
        idx = random.randint(0,10_000)
        if arr[idx] == 1:
            print(f"1 was found at index {idx}")
            break
        elif arr[idx] != 1:
            k -= 1
            if k == 0:
                print(f"Program timed out. Could not locate a 1 after {k} tries.")
                break

def main():
    while True:
        k = int(input("Please enter a limit for the Monte Carlo algorithm: "))
        arr = generate_array()
        find_one(arr, k)
        
main()