def binary_search(list, item):
    lower = 0
    higher = len(list) - 1

    while lower <= higher:
        middle = int((lower + higher) / 2)
        guess = list[middle]

        if guess == item:
            return middle

        if guess > item:
            higher = middle - 1
        else:
            lower = middle + 1
        print('iterating...')

    return None

if __name__ == '__main__':

    # Worst case scenario
    n = 256
    item = 255
    num_list = list(range(0, n))

    print(f'Position of item {item}: {binary_search(num_list, item)}')
