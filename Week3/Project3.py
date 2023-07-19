def tribo(n):
    a, b, c = 1, 1, 1
    if (n < 4):
        return 1
    for i in range(3, n):
        a, b, c = c, b + c, a + b
    return c

def main():
    n = int(eval(input("Choose an Integer: ")))
    print(f"The {n}-th element of Fibonacci is {tribo(n)}")