def containsDuplicate(nums):
    s = set()
    for i in nums:
        s.add(nums[i])
    if len(nums) > len(s):
        return True 
    return False


print(containsDuplicate([1,2,3,1]))
    
