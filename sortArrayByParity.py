def sortArrayByParity(nums):
    i = 0
    j = len(nums) - 1
    while i < j:
        if nums[i]%2 == 0:
            i+=1
        elif nums[j]%2!=0:
            j-=1
        else:
            nums[i],nums[j] = nums[j],nums[i]
    return nums
    

      

print(sortArrayByParity([8, 3, 6, 4, 7, 1, 9, 5]))