def findMedianSortedArrays(nums1: list[int], nums2: list[int]) -> float:
    combined = nums1 + nums2
    combined.sort()
    if len(combined) % 2 != 0:
        return combined[int(len(combined)/2)]
    else:
        center = int(len(combined)/2)
        m1 = combined[center]
        m2 = combined[center-1]
        return (m1+m2)/2

print(findMedianSortedArrays([1,3], [2]))
print(findMedianSortedArrays([1,2], [3,4]))