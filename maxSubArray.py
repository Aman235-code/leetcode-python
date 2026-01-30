def maxSubArray(nums):
    maxS = 0
    curS = 0
    for i in range(len(nums)):
        curS = curS + nums[i]
        if curS < 0:
            curS = 0
        maxS = max(maxS, curS)
    return maxS



print(maxSubArray([1]))