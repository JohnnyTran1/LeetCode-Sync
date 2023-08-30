class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # Problem # 1 
        # n = len(nums)
        # for i in range(n -1):
        #     for j in range(i + 1, n):
        #         if nums[i] + nums[j] == target:
        #             return [i,j]
        # return[]

        # Problem # 2
        # numMap = {}
        # n = len(nums)

        # for i in range(n):
        #     numMap[nums[i]] = i

        # for i in range(n):
        #     complement = target - nums[i]
        #     if complement in numMap and numMap[complement] != i:
        #         return[i,numMap[complement]]

        # return []

        # Problem # 3 
        seen = {}
        for i, value in enumerate(nums): 
            remaining = target - nums[i]

            if remaining in seen: 
                return [i, seen[remaining]]
            else:
                seen[value]=i