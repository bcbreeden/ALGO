def binary_serach(array, target):
    # Assumes the array is already sorted
    lo = 0
    hi = len(array)-1

    while(lo<=hi):
        mid = int((lo+hi)/2)
        if array[mid] == target:
            return True
        elif array[mid] > target:
            hi = (mid - 1)
        else:
            lo = (mid + 1)
    
    return False

print(binary_serach([1,5,6,9,15], 9)) #True
print(binary_serach([1,5,6,9,15], 35)) #False
print(binary_serach([1,5,6,9,15], -49)) #True
print(binary_serach([1,5,9,15], 9)) #True
print(binary_serach([], 6)) #False