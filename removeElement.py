from typing import List


def removeElement(nums: List[int], val: int) -> int:
    new_list = list(filter(lambda x: x != val, nums))
    return len(new_list)

nums = [3,2,2,3]
val = 3
print(removeElement(nums, val))

def searchInsert(nums: List[int], target: int) -> int:
        if target in nums:
            return nums.index(target)
        else:
            left, right = 0, len(nums)-1
            while left <= right:
                mid = left + right // 2
                print(mid)
                if mid == len(nums)-1:
                    if nums[mid] < target:
                        return mid+1
                    else:
                        return mid
                elif nums[mid-1] < target:
                    if nums[mid] == target:
                        return mid
                    elif nums[mid] < target:
                        return mid+1
                    else:
                        return mid
                elif nums[mid] < target:
                    left = mid + 1
                else:
                    right = mid - 1
        return 0

print(searchInsert([1,3,5], 6))