def min_moves(n):
    """
    min_moves(): Uses recursion to find the minimal number of moves with a basecase of T(1) = 1 and
    recursive formula T(n) = 2T(n-1) + 1.
    Takes a positive integer as an input n.
    """
    if n < 2:
        return n
    else:
        return 2 * min_moves(n-1) + 1

def main():
    """
    main(): Uses a while loop to continually ask for a positive integer and calls min_moves()
    on that input.
    """
    while True:
        try:
            n = int(input("Please enter a postive integer: "))
            if n > 0:
                ans = min_moves(n)
                print(f"The minimum number of moves is {ans}")
            else: 
                break
        except: print("Please enter an integer > 0")
main()