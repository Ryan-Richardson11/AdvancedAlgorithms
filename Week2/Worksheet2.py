import random

def generate_vector():
    """
    generate_vector(): 
    Creates an empty list then appends a random number from -500 to 500, 1,000,000 times. The vector is then returned.
    """
    vector = []
    for i in range(0, 1_000_000):
        vector.append(random.randint(-500, 500))
    return vector

def is_unique(n):
    for i in range(len(n)):
        for j in range(len(n)):
            if n[i] == n[j+1]:
                return "Not Unique"
            else:
                return "Unqiue"
            
def main():
    v = generate_vector()
    print(is_unique(v))
    
main()