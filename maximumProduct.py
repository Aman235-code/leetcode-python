def maximumProduct(nums):
    nums.sort()
    i = 0
    j = 1
    print(nums)
    # max = nums[0] * nums[1] * nums[2]
    max = 0
    k = j + 1
    while k < len(nums):
        prod = nums[i] * nums[j] * nums[k]
        print(prod, max)
        if prod > max:
            max = prod
        k+=1
    return max
       

print(maximumProduct([-8,-7,-2,10,20]))