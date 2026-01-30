def intersection(nums1, nums2):
    s1 = set(nums1)
    s2 = set()
    for i in range(len(nums2)):
        if nums2[i] in s1:
            s2.add(nums2[i])
    return list(s2)
             

print(intersection([4,9,5], [9,4,9,8,4]))