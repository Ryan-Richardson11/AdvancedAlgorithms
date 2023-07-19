def tribo(n):
    a, b, c = 1, 1, 1
    if (n < 4):
        return 1
    for i in range(3, n):
        a, b, c = b, c, a + b + c
    return c

def main():
        while True:
            try:
                n = int(eval(input("Choose a Positive Integer: ")))
                if n > 0:
                    print(f"The {n}-th element of Tribonacci is {tribo(n)}")
                else:
                    break
            except: print("Please enter an integer > 0")

main()