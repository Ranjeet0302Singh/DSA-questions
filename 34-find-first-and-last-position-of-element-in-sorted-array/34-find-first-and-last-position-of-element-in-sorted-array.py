class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
    
        def FirstOcc(arr,size,key):

            start=0
            ans=-1
            end=len(nums)-1
            mid=start+(end-start)//2
            while(start<=end):
                if arr[mid]==target:
                    ans=mid
                    end=mid-1
                elif arr[mid]>target:
                    end=mid-1;
                else:
                    start=mid+1
                mid=start+(end-start)//2
            return ans
        def LastOcc(arr,size,key):
            start=0
            ans1=-1
            end=len(nums)-1
            mid=start+(end-start)//2
            while(start<=end):
                if arr[mid]==target:
                    ans1=mid
                    start=mid+1
                elif arr[mid]>target:
                    end=mid-1;
                else:
                    start=mid+1
                mid=start+(end-start)//2
            return ans1


        List=[]
        temp1=FirstOcc(nums,len(nums),target)
        temp2=LastOcc(nums,len(nums),target)
        
        List.append(temp1)
        List.append(temp2)
        
        return List
        
    
        