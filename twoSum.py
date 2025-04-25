from typing import List


def twoSum(nums: List[int], target: int) -> List[int]:
    for num in nums:
        if target - num in nums:
            print(num)
            if nums.count(target - num) > 1:
                return [i for i, x in enumerate(nums) if x == target - num]
            if nums.index(num) != nums.index(target - num):
                return [nums.index(num), nums.index(target - num)]
    return []
    
nums = [3, 2, 4]
target = 6

print(twoSum(nums, target))