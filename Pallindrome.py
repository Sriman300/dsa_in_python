class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False

        def rev(n,r=0):
            if n == 0:
                return r
            return rev(n//10,r*10+n%10)
        return x == rev(x)
