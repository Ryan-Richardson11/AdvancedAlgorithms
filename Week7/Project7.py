import random
import math
log2 = math.log2

def myFunction(x):
    if (x == 0):
        return 0
    elif ((log2(x) * 7) % 17) < (x % 13):
        return (x + log2(x))**3
    elif ((log2(x) * 5) % 23) < (x % 19):
        return (log2(x) * 2)**3
    else:
        return (log2(x)**2) - x

def randomIndex():
    return random.randint(1, 9998)
    
def hillClimb(arr, start_index):
    if start_index == 0 or start_index == len(arr) - 1:
        return arr[start_index]
    
    while arr[start_index] <= arr[start_index+1]:
        start_index += 1
    
    while arr[start_index] <= arr[start_index-1]:
        start_index -= 1

    if arr[start_index] >= arr[start_index-1] and arr[start_index] >= arr[start_index+1]:
        return start_index, arr[start_index]

def main():
    arr = [myFunction(i) for i in range(0, 10000)]
    idx = randomIndex()
    print(f"Random starting index: {idx}")
    ans_index, ans_value = hillClimb(arr, idx)
    print(f"The local Maximum is {ans_value} at index {ans_index}")

if __name__ == "__main__":
    main()