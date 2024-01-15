def moveZeros(nums:list[int]) -> None:
    if len(nums) == 0:
        return None
    
    slow, fast = 0, 1
    while fast < len(nums):
        if nums[slow] == 0 and nums[fast] != 0:
            nums[slow] = nums[fast]
            nums[fast] = 0
            slow += 1
        fast += 1

    return nums


print(moveZeros([0,1,2,0,1,3,2,0]))
