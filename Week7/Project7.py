import random
import math
log2 = math.log2

def myFunction(x):
    """
    Psuedorandom number generator to insert into an array.
    Parameters: A number, in this case through a range.
    """
    if (x == 0):
        return 0
    elif ((log2(x) * 7) % 17) < (x % 13):
        return (x + log2(x))**3
    elif ((log2(x) * 5) % 23) < (x % 19):
        return (log2(x) * 2)**3
    else:
        return (log2(x)**2) - x

def randomIndex():
    """
    Returns a random index between 1 and 9998 as the starting point.
    Avoids edge cases for the random starting point.
    """
    return random.randint(1, 9998)
    
def hillClimb(arr, start_index):
    """
    Uses while loops to check if the number to the right or left is bigger and finds
    the local maximum. Will traverse shoulders starting right first.
    Parameters: An array and random starting index.
    """
    if start_index == 0 or start_index == len(arr) - 1:
        return arr[start_index]
    
    while arr[start_index] <= arr[start_index+1]:
        start_index += 1
    
    while arr[start_index] <= arr[start_index-1]:
        start_index -= 1

    if arr[start_index] >= arr[start_index-1] and arr[start_index] >= arr[start_index+1]:
        return start_index, arr[start_index]

def main():
    """
    main(): Calls my function in range 10000 to get the random generated array. Then calls randomIndex()
    to use as parameters for hillClimb().
    """
    arr = [myFunction(i) for i in range(0, 10000)]
    idx = randomIndex()
    print(f"Random starting index: {idx}")
    ans_index, ans_value = hillClimb(arr, idx)
    print(f"The local Maximum is {ans_value} at index {ans_index}")

if __name__ == "__main__":
    main()