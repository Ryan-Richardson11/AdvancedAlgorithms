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

def selection(v):
    indexing_length = range(0, len(v)-1)
    for i in indexing_length:
        min_value = i
        for j in range(i+1, len(v)):
            if v[j] < v[min_value]:
                min_value = j
        if min_value != i:
            v[min_value], v[i] = v[i], v[min_value]
    return v

def main():
    v = generate_vector()
    sorted = selection(v)
    print(sorted)

if __name__ == "__main__":
    main()