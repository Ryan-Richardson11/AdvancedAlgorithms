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

def is_unique_brute(n):
    """
    is_unique(): Uses brute for to iterate through the vector and check if any of the values match.
    Takes 1 vector as an argument and returns Not Unique or Unique.
    """
    for i in range(len(n)):
        for j in range(i+1, len(n)):
            if n[i] == n[j]:
                return "Not Unique"
    return "Unqiue"
            
def is_unique_trans(n):
    """
    is_unique(): Uses transform and conquer algorithm to check if any of the values match.
    Takes 1 vector as an argument and returns Not Unique or Unique.
    """
    for i in range(len(n)):
        for j in range(i+1, len(n)):
            if n[i] == n[j]:
                return "Not Unique"
    return "Unqiue"

def main():
    """
    main(): Stores a generated vector in the variable v, then prints it and passes it through is_unique as an argument.
    """
    v = generate_vector()
    print(v)
    print(is_unique_brute(v))
    
main()