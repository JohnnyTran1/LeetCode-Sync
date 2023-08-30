class Solution:
    def validPalindrome(self, s: str) -> bool:
        # Number # 1 
        # p1 = 0
        # p2 = len(s) - 1
        # while p1<= p2:
        #     if s[p1] !=s [p2]:
        #         string1=s[:p1] +s[p1+1:]
        #         string2=s[:p2] +s[p2+1:]
        #         return string1==string1[::-1] or string2==string2[::-1]
        #     p1+=1
        #     p2-=1
        # return True

        # Number # 2 
        # def verify(s, left, right, deleted):
        #     while left < right:
        #         if s[left] != s[right]:
        #             if deleted:
        #                 return False
        #             else:
        #                 return verify(s, left+1, right, True) or verify(s, left, right-1, True)
        #         else:
        #             left += 1
        #             right -= 1
        #     return True
        # return verify(s, 0, len(s)-1, False)

        # Number # 3
            def isPalindrome(left, right, s, count):
                while left < right:
                    if s[left] != s[right]:
                        if count == 1:
                            return False
                        return isPalindrome(left + 1, right, s, count + 1) or isPalindrome(left, right -1, s, count +1)
                    left += 1
                    right -= 1
                return True
            return isPalindrome(0, len(s) - 1, s, 0)

        # Number # 3 

        # Number # 4 
