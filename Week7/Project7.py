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
    if start_index == 0:
        return arr[start_index]
    elif start_index == len(arr) - 1:
        return arr[start_index]
    elif arr[start_index] > arr[start_index-1] and arr[start_index] > arr[start_index+1]:
        return arr[start_index]
    elif arr[start_index] <= arr[start_index+1]:
        return hillClimb(arr, start_index+1)
    else:
        return hillClimb(arr, start_index-1)

def main():
    arr = []
    for i in range(0, 10000):
        arr.append(myFunction(i))

    idx = randomIndex()
    print(f"Random starting index: {idx}")
    ans = hillClimb(arr, idx)
    print(f"The local Maximum is {ans} at index {arr.index(ans)}")

main()