class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        Sum=0
        product=1 
        while n>0:
            temp=n%10
            product=product*temp
            Sum=Sum+temp
            n=n//10
        return product-Sum