import random

def generate_vector():
    """
    generate_vector(): 
    Creates an empty list then appends a random number from 1 to 1,000,000, 1,000 times. The vector is then returned.
    """
    vector = []
    for i in range(0, 1000):
        vector.append(random.randint(1, 1_000_000))
    return vector

def is_unique(n):
    """
    """
    for i in range(len(n)):
        for j in range(i+1, len(n)):
            if n[i] == n[j]:
                return "Not Unique"
    return "Unqiue"
            
def main():
    v = generate_vector()
    print(v)
    print(is_unique(v))
    
main()