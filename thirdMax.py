def thirdMax(nums):
    nums.sort(reverse=True)
    s = set(nums)
    lst = list(s)
    lst.sort(reverse=True)
    print(lst)
    if len(lst) < 2:
        return max(lst)
    return lst[2]

print(thirdMax([1,2]))