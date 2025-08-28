class Solution:
    def longestSubarray(self, arr, k):  
        dict1={0:-1}
        sm,ans=0,0
        for i in range(len(arr)):
            sm+=arr[i]
            if sm-k in dict1:
                ans=max(ans,i-dict1[sm-k])
            if sm not in dict1:
                dict1[sm]=i
        return ans