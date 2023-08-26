# class Solution:
#     def containsDuplicate(self, nums: List[int]) -> bool:
#         nums.sort()
#         n = len(nums)
#         for i in range(1, n):
#             if nums[i] == nums[i - 1]:
#                 return True
#         return False

# class Solution:
#     def containsDuplicate(self, nums: List[int]) -> bool:
#         return len(set(nums))!=len(nums)

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        hashset = set()

        for n in nums:
            if n in hashset:
                return True
            hashset.add(n)
        return False