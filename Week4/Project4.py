# knapsack unbounded - Greedy approach

def knapsack(name, value, height, width, depth, cap):
    """
    knapsack(): Calculates volume per volume ratio and sorts list from high to low.
    Returns best item while still less than the capacity.
    Parameters: name, value, height, width, depth, cap.
    """
    rvv = []         # triplet ratio, volume, value, index
    for i in range(len(value)):
        # Change to a function
        volume = height[i] * width[i] * depth[i] 
        rvv.append([name[i], value[i] / volume, volume, value[i], i])
    rvv.sort(key=lambda x: x[1], reverse=True)    # sort from high to low ratio
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

def read_file(file_path):
    """
    read_file(): Reads lines from a csv file and appends each to a list for each index.
    Returns name, value, height, width, depth
    """
    name, value, height, width, depth = [], [], [], [], []
    with open(file_path, "r", encoding="utf-8-sig") as my_file:
        for line in my_file:
            info = line.strip().split(",")
            name.append(info[0])
            value.append(int(info[1]))
            height.append(int(info[2]))
            width.append(int(info[3]))
            depth.append(int(info[4]))
    return name, value, height, width, depth

def main():
    """
    Calls read_file method on file path.
    While loop controls flow for user capacity input, breaks if number < 1 is entered.
    Prints Items, total value, and square inches left unused.
    """
    file_path = "C:\\Users\\Ryan\\Desktop\\AdvancedAlgorithms\Week4\\packs.csv"
    name, value, height, width, depth = read_file(file_path)
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