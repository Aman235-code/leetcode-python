def thirdMax(nums):
    firstSum = -1 
    secondSum = -1 
    thirdSum = -1 
    for i in range(len(nums)):
        
        if (nums[i] == firstSum) or (nums[i] == secondSum) or (nums[i] == thirdSum):
            continue

        if nums[i] > firstSum:
            firstSum = nums[i]
            print("fs ",firstSum)
        elif nums[i] > secondSum:
            secondSum = nums[i]
            print("ss ",secondSum)
        else:
            thirdSum = nums[i]
            print("ts ",thirdSum)
            
               
    return firstSum if thirdSum < 0 else thirdSum


print(thirdMax([-2147483648,1,1]))