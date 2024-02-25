def searchLowest(arr):
    lowest = arr[0]
    lowest_index = 0
    for i in range(1, len(arr)):
        if arr[i] < lowest:
            lowest = arr[i]
            lowest_index = i
    return lowest_index

def selectionSort(arr):
    newArr = []
    for i in range(len(arr)):
        lowest = searchLowest(arr)
        newArr.append(arr.pop(lowest))
    return newArr

if __name__ == '__main__':
    print(selectionSort([5, 3, 6, 2, 10]))
