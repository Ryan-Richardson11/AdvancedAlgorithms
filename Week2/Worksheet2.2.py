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

    for i in range(len(a)):
        counter = a.count(a[i])
        if counter > max_count:
            max_count = counter
            mode = a[i]
    return mode

def main():
    a = [3, 3, 3, 2, 5, 76, 734, 23, 5, 5, 4, 3, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4]
    print(find_mode_brute(a))
    print(find_mode(a))
main()
