# a function that takes a list and target parameter
# multiple variables : middle, start, end, steps
def binary_search(list, element):
    middle = 0
    start = 0
    end = len(list)
    steps = 0

    # recursion or while loop
    while start <= end:
        print("Step", steps, ":", str(list[start:end+1]))

        # increase the steps each time a split is done
        steps = steps + 1
        middle = (start + end) // 2

        # conditions to track target position
        if element == list[middle]:
            return middle
        if element < list[middle]:
            end = middle - 1
        else:
            start = middle + 1

    return -1


my_list = list(range(1, 3044, 3))
target = 2

binary_search(my_list, target)
