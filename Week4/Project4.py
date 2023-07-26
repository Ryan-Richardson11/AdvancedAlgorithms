# # knapsack unbounded - Greedy approach

def knapsack(name, value, height, width, depth, cap):
    rwv = []         # triplet ratio, weight, value, index
    for i in range(len(value)):
        volume = height[i] * width[i] * depth[i]
        rwv.append([name[i], value[i] / volume, volume, value[i], i])
    rwv.sort(reverse=True)    # sort from high to low rate
    print(rwv)
    ans = []                     # the list of added items
    tv = 0                                  # total weight
    found = True
    while found:        # until no fitting item is found
        found = False
        for t in rwv:              # search an item to add
            if (t[2] + tv) <= cap:      # if the item fits
                ans.append(t[0])                  # add it
                tv += t[2]
                found = True
                break
    return ans           # returns the list of added items

def main():
    my_file = open("C:\\Users\\Ryan\\Desktop\\AdvancedAlgorithms\Week4\\Project4.csv", "r")
    name, value, height, width, depth = [], [], [], [], []
    for line in my_file:
        info = line.strip().split(",")
        name.append(info[0])
        value.append(int(info[1]))
        height.append(int(info[2]))
        width.append(int(info[3]))
        depth.append(int(info[4]))
    
    print(knapsack(name, value, height, width, depth, 100))
    
main()