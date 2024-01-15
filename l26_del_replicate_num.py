# 快慢指针
# 将不符合要求的数扔到最后

def removeDuplicates(nums: list[int]) -> int:
    if len(nums) == 0:
        return 0 
    slow = 0 
    fast = 1 
    while fast < len(nums):
        if nums[slow] != nums[fast]:
            slow += 1 
            nums[slow] = nums[fast]
        fast += 1

    return slow + 1

print(removeDuplicates([1,2,4,5,6,6]))
print(removeDuplicates([0,0,2,2,3,3]))


