from typing import List

# Первый алгоритм, рабочий, но медленный (O(n))
def searchInsert(nums: List[int], target: int) -> int:
    if target in nums:
            return nums.index(target)
    else:
        i = 1
        while not target-i in nums and i <= nums.__len__():
            i += 1
        if target-i+1 < 0 or i > nums.__len__():
            return 0
        return nums.index(target-i)+1

# Второй алгоритм, ускоряемся
# Прошлый алгоритм имел скорость O(n) в худшем случае
# Попробуем бинарным поиском, O(log(n))
def searchInsertBinary(nums: List[int], target: int) -> int:
    left, right = 0, len(nums) - 1 
    while left <= right: 
        mid = left + (right - left) // 2 
        if nums[mid] == target:
            return mid
        elif nums[mid] > target:
            right = mid - 1
        else:
            left = mid + 1
    return left