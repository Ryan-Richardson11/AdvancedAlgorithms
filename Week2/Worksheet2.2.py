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

def find_mode_brute(a):
    max_value, max_count = 0, 0
    for i in range(len(a)):
        count = 0
        for j in range(len(a)):
            if (a[i] == a[j]):
                count += 1
        if (count > max_count):
            max_count = count
            max_value = a[i]
    return max_value

def find_mode(a):
    mode = None
    max_count = 0
    a.sort()

    count = 0
    for i in range(len(a)):
        if i < len(a) - 1 and a[i] == a[i+1]:
            count += 1
        else:
            count = 0
        if count > max_count:
            max_count = count
            mode = a[i]
    return mode

# def find_mode_set(a):
#     mode = None
#     max_count = 0
#     distinct_values = set(a)

#     for value in distinct_values:
#         counter = a.count(value)
#         if counter > max_count:
#             max_count = counter
#             mode = value

#     return mode

def main():
    a = generate_array()

    print(find_mode_brute(a))
    print(find_mode(a))
    # print(find_mode_set(a))

main()
