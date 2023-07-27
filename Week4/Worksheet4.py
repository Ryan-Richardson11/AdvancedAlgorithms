# Egyptian fraction Greedy
from math import ceil
  
# n is the numerator, d is the denominator
def egyptian(n, d):
  
    print("The Egyptian Fraction of {}/{}".format(n, d))
    ans = []
    # while numerator is not 0
    while (n > 0):
        x = ceil(d / n)          # compute the minimal larger denominator
        ans.append(x)            # hold it to the numerator list
        n, d = x * n - d, d * x  # update the remainder to n and d
    for a in ans:
        print("1/{}".format(a), end=" ")

def main():
    print("Greedy Algorithm to Compute Egytian Fractions")
    # Results 1/2 1/3
    egyptian(5, 6)
    print("\n")
    # Results 1/3 1/8 1/120
    egyptian(7, 15)
    print("\n")
    # Results 1/2 1/6 1/102
    egyptian(23, 34)
    print("\n")
    # Results 1/3 1/23 1/7383
    egyptian(121, 321)
    print("\n")
    # Results 1/25 1/1538 1/4729350
    egyptian(5, 123)

main()