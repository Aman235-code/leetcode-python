def findDifference(nums1, nums2):
    s1 = set(nums1)
    s2 = set(nums2)
    l1 = list(s1)
    l2 = list(s2)

    res1 = [nums for nums in l1 if nums not in s2]
    res2 = [nums for nums in l2 if nums not in s1]
    return [res1, res2]


nums1 = [1,2,3,3] 
nums2 = [1,1,2,2]
print(findDifference(nums1, nums2))