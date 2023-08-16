import random

def generate_array():
    arr = []
    for i in range(10_000):
        arr.append(random.randint(0,1))
    return arr

def find_one(arr):
    while True:
        idx = random.randint(0,10_000)
        if arr[idx] == 1:
            print(f"1 was found at index {idx}")
            break

def main():

    arr = generate_array()
    find_one(arr)
    
main()