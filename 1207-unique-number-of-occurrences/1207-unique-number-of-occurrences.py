class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        arr=Counter(arr)
        print(arr)
        arrValue=set(Counter(arr).values())
        arrkey=set(Counter(arr).keys())
        print(arrValue)
        print(arrkey)
        if len(arrkey) == len(arrValue):
            return True
        else:
            return False