class Solution:
    def largestTriangleArea(self, points: List[List[int]]) -> float:
        def areatri(a,b,c):
            return abs(a[0]*b[1]+b[0]*c[1]+c[0]*a[1]-(a[0]*c[1]+c[0]*b[1]+b[0]*a[1]))
        L = len(points)
        A = 0
        for i in range(L-2):
        	for j in range(i+1,L-1):
        		for k in range(j+1,L):
        			a = areatri(points[i],points[j],points[k])
        			if a > A:
        				A = a
        return(A/2)
