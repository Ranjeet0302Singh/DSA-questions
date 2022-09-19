class Solution:
    def arraySign(self, nums: List[int]) -> int:
        def signFunc(x):
            if x==0:
                return 0
            elif x>0:
                return 1
            else:
                return -1
        product=math.prod(nums)
        return signFunc(product)
        