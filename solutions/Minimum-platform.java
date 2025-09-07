class Solution {
    static int findPlatform(int arr[], int dep[]) {
        int n=arr.length;
        Arrays.sort(arr);
        Arrays.sort(dep);
        int i=0, j=0;
        int platforms_needed=0, max_platforms=0;
        while (i < n && j<n){
            if(arr[i] <= dep[j]){
                platforms_needed++;
                i++;
            }else{
                platforms_needed--;
                j++;}
            max_platforms=Math.max(max_platforms, platforms_needed);
        }
        return max_platforms;
    }
}
