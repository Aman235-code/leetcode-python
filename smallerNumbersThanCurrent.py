def smallerNumbersThanCurrent(nums):
    nl = []
    for v in nums:
        c = [i for i in nums if v > i]
        nl.append(len(c))
    return nl


print(smallerNumbersThanCurrent([7,7,7,7]))
     
