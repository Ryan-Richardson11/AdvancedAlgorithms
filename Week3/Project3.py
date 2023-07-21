def tribo(n):
    """
    tribo(n): Efficient dynamic programmming algorithms to solve fibonacci but adding the previous 3 integers instead of two.
    Takes an input n to find the nth elements Tribonacci number.
    """
    a, b, c = 1, 1, 1
    if (n < 4):
        return 1
    for i in range(3, n):
        a, b, c = b, c, a + b + c
    return c

def main():
        """
        main(): Continually asks for a positive integer in a while loop and uses that as n to call tribo().
        Try-except loop to catch any input errors.
        """
        while True:
            try:
                n = int(eval(input("Choose a Positive Integer: ")))
                if n > 0:
                    print(f"The {n}-th element of Tribonacci is {tribo(n)}")
                else:
                    break
            except: print("Please enter an integer > 0")

main()