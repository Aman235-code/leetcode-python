def missingNumber(nums):
    nums.sort()
    for i, v in enumerate(nums):
        if i!= v:
            return v-1
        if i == len(nums)-1:
            return v+1

#  = sum(range(len(nums)+1)) - sum(nums)
# return valval