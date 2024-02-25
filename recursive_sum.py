def sum(arr):
    if arr == []:
        return 0
    return arr[0] + sum(arr[1:])

if __name__ == '__main__':
    print(sum([2, 4, 6, 10, 15, 1, 45, 69, 17]))
