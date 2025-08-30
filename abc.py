

// User function Template for Java

class Solution {
    static int majorityElement(int arr[]) {
        int candidate=-1, count=0;
        for(int num:arr){
            if(count==0){
                candidate = num;
            }
            count += (num== candidate) ? 1:-1;
        }
        count=0;
        for(int num: arr){
            if(num==candidate) {
                count++;
            }
        }
        return (count> arr.length/2) ? candidate : -1;
        // code here
        
    }
}