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
    a = [2, 5, 2, 3, 4, 7, 3]
    print(find_mode(a))


main()
