def majorityElement(nums):
    count = 0
    cand = nums[0]
    for i in range(len(nums)):
        if cand != nums[i]:
            count -= 1
            if count < 0:
                cand = nums[i]
                count = 0
        else:
            count +=1
    return cand


print(majorityElement([2,2,1,1,1,2,2]))
     