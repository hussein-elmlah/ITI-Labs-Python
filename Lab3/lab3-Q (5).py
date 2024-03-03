class Solution(object):
    def searchInsert(self, nums, target):
        target_index = nums.index(target) if target in nums else -1
        if target_index != -1:
            return target_index
        for i in range(len(nums)):
            if target <= nums[i]:
                nums.insert(i, target)
                return i
        nums.append(target)
        return len(nums) - 1
