import random

def generate_vector():
    """
    generate_vector(): 
    Creates an empty list then appends a random number from -100 to 100, 1000 times. The vector is then returned.
    """
    vector = []
    for i in range(0, 999):
        vector.append(random.randint(-1000, 1000))
    return vector

def swap(A, i, j):
    """
    Input: An array A and indicies i and j.
    Output: An array where A[i] and A[j] have been swapped.
    """
    temp = A[i]
    A[i] = A[j]
    A[j] = temp

def bubble_sort(A):
    """
    Input: An array of A integers.
    Output: An array A sorted in increasing order.
    """
    for i in range(len(A)-1):
        for j in range(len(A)-i-1):
            if A[j+1] < A[j]:
                swap(A, j+1, j)


def main():
    v = generate_vector()
    sorted = bubble_sort(v)
    print(sorted)

if __name__ == "__main__":
    main()