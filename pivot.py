def pivotIndex(nums):
    leftSum = 0
    s = sum(nums)
    res = 0
    for i in range(len(nums)):
        res = s - leftSum - nums[i]
        if res == leftSum:
            return i   
        leftSum = leftSum + nums[i]
    return -1


print(pivotIndex([1,7,3,6,5,6]))


