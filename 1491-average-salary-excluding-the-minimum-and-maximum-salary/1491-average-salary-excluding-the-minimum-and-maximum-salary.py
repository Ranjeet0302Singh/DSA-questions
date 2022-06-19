class Solution:
    def average(self, salary: List[int]) -> float:
        MinSalary=min(salary)
        MaxSalary=max(salary)
        salary.remove(MinSalary)
        salary.remove(MaxSalary)
        ans=sum(salary)/len(salary)
        return ans
        