def twoSum(nums, target):
    left = 0
    right = len(nums)-1

    while left < right:
        tot = nums[left] + nums[right]

        if tot == target:
            return [left, right]
        if tot < target:
            left += 1
        else:
            right -= 1


print(twoSum([1,2,4,6,8,11,15], 10))

 
        

