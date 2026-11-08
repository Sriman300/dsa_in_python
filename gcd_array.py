class Solution:
    def findGCD(self, nums: list[int]) -> int:
        nums.sort()

        sml = nums[0]
        lar = nums[-1]

        def gcd(a,b):
            if b == 0:
                return a

            return gcd(b , a % b)


        return gcd(sml,lar)
