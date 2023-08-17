import math
log2 = math.log2

def myFunction(x):
    if (x == 0):
        return 0
    elif ((log2(x) * 7) % 17) < (x % 13):
        return (x + log2(x))**3
    elif ((log2(x) * 5) % 23) < (x % 19):
        return (log2(x) * 2)**3
    else:
        return (log2(x)**2) - x


def main():
    arr = []
    for i in range(0, 1000):
        arr.append(myFunction(i))
    print(arr)

main()