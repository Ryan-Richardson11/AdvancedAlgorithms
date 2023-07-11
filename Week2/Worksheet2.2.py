a = []

def find_mode(a):
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