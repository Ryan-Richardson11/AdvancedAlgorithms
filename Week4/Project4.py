# # knapsack unbounded - Greedy approach

def knapsack(name, value, height, width, depth, cap):
    rvv = []         # triplet ratio, volume, value, index
    for i in range(len(value)):
        # Change to a function
        volume = height[i] * width[i] * depth[i] 
        rvv.append([name[i], value[i] / volume, volume, value[i], i])
    rvv.sort(reverse=True)    # sort from high to low rate
    ans = []                     # the list of added items
    tv = 0                                  # total volume
    found = True
    while found:        # until no fitting item is found
        found = False
        for t in rvv:              # search an item to add
            if (t[2] + tv) <= cap:      # if the item fits
                ans.append(t[0])                  # add it
                tv += t[2]
                found = True
                break
    return ans           # returns the list of added items

def main():
    """
    Reads lines from a csv file and appends each to a list
    """
    my_file = open("C:\\Users\\Ryan\\Desktop\\AdvancedAlgorithms\Week4\\packs.csv", "r", encoding="utf-8-sig")
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
            item_counts = {item: answer.count(item) for item in set(answer)}
            items_str = ", ".join([f"{count} {item}" for item, count in item_counts.items()])
            for a in answer:
                idx = name.index(a)
                volume = height[idx] * width[idx] * depth[idx]
                print(f"Item: {name[idx]} Value: {value[idx]} - Volume: {volume}")
                tval += value[idx]
                tvol += volume
            print(f"The suggested items are: {items_str} with a total value of ${tval}. There were {capacity - tvol} square inches left unused.")
    
main()

