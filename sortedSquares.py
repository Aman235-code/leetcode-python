def sortedSquares(nums):
    res = list([0]*len(nums))
    l = 0
    r = len(nums) - 1
    k = r
    while(k>=0):
        if nums[l]**2 < nums[r] ** 2:
            res[k] = nums[r] ** 2
            r-=1
        else:
            res[k] = nums[l] ** 2
            l+=1
        k-=1
    return res

nums = [-4,-1,0,3,10]
print(sortedSquares(nums))