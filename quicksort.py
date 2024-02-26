def quicksort(array):
    if len(array) < 2:
        return array
    else:
        pivot = array[0]
        lower_numbers = [i for i in array[1:] if i <= pivot]
        higher_numbers = [i for i in array[1:] if i > pivot]
        return quicksort(lower_numbers) + [pivot] + quicksort(higher_numbers)

if __name__ == '__main__':
    print(quicksort([10, 5, 2, 3]))
