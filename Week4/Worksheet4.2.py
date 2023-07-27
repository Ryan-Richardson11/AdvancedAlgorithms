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
    """
    The reason it is not as accurate as computing by hand may be because python has a
    very slight rounding error and that may show up in very large numbers such as the final fraction in this example.

    Results 1/25 1/757 1/763309 1/873960180913 1/1527612795642093385023488
    """
    egyptian(5, 121)
    
main()