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

def is_unique_brute(a):
    """
    is_unique(): Uses brute for to iterate through the vector and check if any of the values match.
    Takes 1 vector as an argument and returns Not Unique or Unique.
    """
    ans = True
    for i in range(len(a)):
        for j in range(len(a)):
            if (i != j) and (a[i] == a[j]):
                ans = False
                break
        if (not ans):
            break
    return ans
            
def is_unique_trans(a):
    """
    is_unique(): Uses transform and conquer algorithm to check if any of the values match.
    Takes 1 vector as an argument and returns Not Unique or Unique.
    """
    a.sort()
    for i in range(len(a)):
        if (a[i-1] == a[i]):
            return False
    return True

def main():
    """
    main(): Stores a generated vector in the variable v, then prints it and passes it through is_unique methods as an argument.
    """
    v = generate_vector()
    print(v)
    print(is_unique_brute(v))
    print(is_unique_trans(v))
    
main()