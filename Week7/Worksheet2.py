import random

def generate_array():
    arr = []
    for i in range(10_000):
        arr.append(random.randint(0,1))
    return arr

def find_one(arr):
    count = 0
    while True:
        idx = random.randint(0,10_000)
        count += 1
        if arr[idx] == 1:
            print(f"1 was found at index {idx} after {count} tries")
            break

def main():

    arr = generate_array()
    find_one(arr)

main()