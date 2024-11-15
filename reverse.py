def reverse_list(items):
    i = 0
    j = len(items)-1
    while i < j:
        temp = items[j]
        items[j] = items[i]
        items[i] = temp
        i = i + 1
        j = j - 1


def swap(x, y):
    temp = x
    x = y
    y = temp


def swap_list_positions(items, i, j):
    temp = items[i]
    items[i] = items[j]
    items[j] = temp


if __name__ == "__main__":
    items = [1,2,3,4]
    reverse_list(items)
    print(items) # fyi, print([1,2]) outputs [1,2]
    swap(items[0], items[3])
    print(items)
    swap_list_positions(items, 0, 3)
    print(items)