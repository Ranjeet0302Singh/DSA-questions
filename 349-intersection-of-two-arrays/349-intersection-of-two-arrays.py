class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1=set(nums1)
        nums2=set(nums2)
        # print(nums1,nums2)
        ans=nums1.intersection(nums2)
        # print(ans)
        ans=list(ans)
        return ans
            
        