# # knapsack unbounded - Greedy approach

def knapsack(name, value, height, width, depth, cap):
    rwv = []         # triplet ratio, weight, value, index
    for i in range(len(value)):
        volume = height[i] * width[i] * depth[i]
        rwv.append([name[i], value[i] / volume, volume, value[i], i])
    rwv.sort(reverse=True)    # sort from high to low rate
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
    my_file = open("C:\\Users\\Ryan\\Desktop\\AdvancedAlgorithms\Week4\\Project4.csv", "r", encoding="utf-8-sig")
    name, value, height, width, depth = [], [], [], [], []
    for line in my_file:
        info = line.strip().split(",")
        name.append(info[0])
        value.append(int(info[1]))
        height.append(int(info[2]))
        width.append(int(info[3]))
        depth.append(int(info[4]))
    while True:
        capacity = int(input("Enter the total capacity: "))
        if capacity < 1:
            break
        else:
            answer = knapsack(name, value, height, width, depth, capacity)
            tvol, tval = 0, 0
            for a in answer:
                idx = name.index(a)
                volume = height[idx] * width[idx] * depth[idx]
                print(f"Item: {name[idx]} Value: {value[idx]} - Volume: {volume}")
                tval += value[idx]
                tvol += volume
            print(f"Items: {len(answer)} - Value: ${tval} - Volume: {tvol} inches squared")
            print(f"The suggested items are {len(answer)} {name[idx]}'s with a total value of ${tval}. There were {capacity - tvol} square inches left unused.")
    
main()
