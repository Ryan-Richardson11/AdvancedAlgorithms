from random import randrange

def test(initialSize, probRemove):
    accCheap, accCosty = 0, 0
    s = initialSize
    m = 2*s
    for i in range(100000):
        if (randrange(100) < probRemove):
            if (s > 0):
                s -= 1
        else:
            if (s == m):
                m = m*2
                s += 1
                accCosty += 1
            else:
                s += 1
                accCheap += 1
    print("Initial size:", initialSize, "Prob Remove:", probRemove, "out of 100")
    print("Costy: {:7} ({:3.1}%)".format(accCosty,accCosty/(accCosty+accCheap)))
    print("Cheap: {:7} ({:3.1}%)".format(accCheap,accCheap/(accCosty+accCheap)))

def main():
    """
    The closest I could get was 0.0002% and 16 costly operations on average for each of the best test cases.
    Ideally you would want the lowest chance of removal to increase costly operations since there will be less space allocated.
    Additionally the smaller the array is to begin with the more costly operations should happen.
    I believe to get a higher number of costly operations it would have to be simulated on a larger range.
    """
    test(10, 1)
    test(0, 1)
    test(1, 10)
    test(1, 1)
    test(1, 0.1)
    test(1, 0.0000000000000000000000000000000000000000000000000000000000000001)
    test(1, 0)

main()