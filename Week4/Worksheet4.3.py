# knapsack unbounded - Greedy approach

def knapsack(v, w, cap):
    rwv = []         # triplet ratio, weight, value, index
    for i in range(len(v)):
        rwv.append([v[i]/w[i],w[i],v[i],i])
    rwv.sort(reverse=True)    # sort from high to low rate
    ans = []                     # the list of added items
    tw = 0                                  # total weight
    found = True
    while (found):        # until no fitting item is found
        found = False
        for t in rwv:              # search an item to add
            if (t[1] + tw) <= cap:      # if the item fits
                ans.append(t[3])                  # add it
                tw += t[1]
                found = True
                break
    return ans           # returns the list of added items

def main():
    values1 = [5, 8, 12]
    weights1 = [10, 20, 30]
    print(knapsack(values1, weights1, 838))
    print("\n")
    values2 = [5, 5, 7, 11, 13]
    weights2 = [17, 23, 29, 31, 37]
    print(knapsack(values2, weights2, 997))
    print("\n")
    values3 = [5, 6, 7, 8]
    weights3 = [25, 36, 49, 64]
    print(knapsack(values3, weights3, 250))
    print("\n")
    values4 = [5, 6, 7, 8]
    weights4 = [25, 36, 49, 64]
    print(knapsack(values4, weights4, 360))
main()