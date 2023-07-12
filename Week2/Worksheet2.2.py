import random

def generate_array():
    """
    generate_array(): 
    Creates an empty list then appends a random number from 1 to 100, 1,000 times. The array is then returned.
    """
    a = []
    for i in range(0, 1000):
        a.append(random.randint(0, 9))
    return a

def find_mode(a):
    """"
    find_mode(): Uses transform and conquer by first sorting the array then iterating through each sequence and adding to a counter.
    Passes an array through as an argument.
    Accounts for multiple modes by appending to a list.
    """
    mode = []
    max_count = 0
    a.sort()

    count = 1
    for i in range(len(a)):
        if a[i-1] == a[i]:
            count += 1
        else:  
            if count > max_count:
                max_count = count
                mode = [a[i-1]]
            elif count == max_count:
                mode.append(a[i-1])
            count = 1
    return mode

def main():
    """
    main(): Calls generate_array to create a random array and passes it through find_mode() to calculate the mode of the array.
    """
    a = generate_array()
    print(find_mode_brute(a))
    print(find_mode(a))


main()
