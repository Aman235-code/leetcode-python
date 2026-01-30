def findDisappearedNumbers(nums):
    num_set = set(nums)
    res = []
    for i in range(1, len(nums)+1):
        if i not in num_set:
            res.append(i)
    return 


findDisappearedNumbers([1,1])