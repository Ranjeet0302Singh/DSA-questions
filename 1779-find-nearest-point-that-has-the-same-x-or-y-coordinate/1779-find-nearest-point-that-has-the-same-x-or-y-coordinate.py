class Solution:
    def nearestValidPoint(self, x: int, y: int, points: List[List[int]]) -> int:
        minDist = math.inf
        index = -1
        for i in range(len(points)):
            if points[i][0]==x or points[i][1]==y:
                manDist = abs(points[i][0]-x)+abs(points[i][1]-y)
                if manDist<minDist:
                    index = i
                    minDist = manDist
        return index