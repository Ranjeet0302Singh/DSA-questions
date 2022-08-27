class Solution:
    def average(self, salary: List[int]) -> float:
        amount=sum(salary)-min(salary)-max(salary)
        lenght=len(salary)-2
        return amount/lenght
        