class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        # return nums*2

        nums.extend(nums)
        return nums
        #The extend() method adds all the element of an iterable ( list , tuple , string etc.) to the end of the list.
