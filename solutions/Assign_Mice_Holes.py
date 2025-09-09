class Solution:
    def assignHole(self, mices, holes):
        maxi=0
        mices.sort()
        holes.sort()
        for i in range(len(mices)):
            maxi=max(maxi,abs(holes[i]-mices[i]))
        return(maxi)