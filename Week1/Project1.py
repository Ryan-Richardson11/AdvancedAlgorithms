import random
import cProfile

def generate_vector(n):
    """
    generate_vector(): 
    Creates an empty list then appends a random number from -100 to 100, 1000 times. The vector is then returned.
    """
    vector = []
    for i in range(n):
        vector.append(random.randint(-1000, 1000))
    return vector

def swap(A, i, j):
    """
    swap(): Helper function for the bubble sort algorithm to swap indicies.
    Input: An array A and indicies i and j.
    Output: An array where A[i] and A[j] have been swapped.
    """
    temp = A[i]
    A[i] = A[j]
    A[j] = temp

def bubble_sort(A):
    """
    bubble_sort(): Sorts a vector using the bubble sort algorithm.
    Input: An array of A integers.
    Output: An array A sorted in increasing order.
    """
    for i in range(len(A)-1):
        for j in range(len(A)-i-1):
            if A[j+1] < A[j]:
                swap(A, j+1, j)
    return A

def main():
    """
    main(): Sorts the vector for each size 1000 to 10000
    """
    v1 = generate_vector(1000)
    sorted = bubble_sort(v1)
    print(sorted)
    print("\n")
    
    v2 = generate_vector(2000)
    sorted = bubble_sort(v2)
    print(sorted)
    print("\n")

    v3 = generate_vector(3000)
    sorted = bubble_sort(v3)
    print(sorted)
    print("\n")

    v4 = generate_vector(4000)
    sorted = bubble_sort(v4)
    print(sorted)
    print("\n")

    v5 = generate_vector(5000)
    sorted = bubble_sort(v5)
    print(sorted)
    print("\n")

    v6 = generate_vector(6000)
    sorted = bubble_sort(v6)
    print(sorted)
    print("\n")

    v7 = generate_vector(7000)
    sorted = bubble_sort(v7)
    print(sorted)
    print("\n")

    v8 = generate_vector(8000)
    sorted = bubble_sort(v8)
    print(sorted)
    print("\n")

    v9 = generate_vector(9000)
    sorted = bubble_sort(v9)
    print(sorted)
    print("\n")

    v10 = generate_vector(10000)
    sorted = bubble_sort(v10)
    print(sorted)
    print("\n")

if __name__ == "__main__":
    cProfile.run("main()")