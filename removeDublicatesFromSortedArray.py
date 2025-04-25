from typing import List


def removeDuplicates(nums: List[int]) -> int:
    k = 0
    for i in range(len(nums)-1, 0, -1):
        if nums[i] == nums[i-1] and i > 0:
            nums.pop(i)
    k = len(nums)
    return(k, nums)

nums = [1,1,2]
print(removeDuplicates(nums))
