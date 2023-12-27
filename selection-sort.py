def selection_sort(array):
    for current_index in range(0, len(array)-1):
        min_index = current_index
        for i in range((current_index+1),len(array)):
            if array[i] < array[min_index]:
                min_index = i
        current_value = array[current_index]
        array[current_index] = array[min_index]
        array[min_index] = current_value
    return array

print(selection_sort([5, 1, 3, 9, 7])) #1, 3, 5, 7, 9
print(selection_sort([])) #[]
print(selection_sort([-12.5, 5, 76, 1.75, -42, 6.1])) #-42, -12.5, 1.75, 5, 6.1, 76