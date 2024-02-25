def item_count(arr):
    if arr == []:
        return 0
    return 1 + item_count(arr[1:])

if __name__ == '__main__':
    print(item_count([2, 4, 6, 10, 15, 1, 45, 69, 17]))
