import java.io.*;
import java.lang.*;
import java.util.*;

class AtleastTwo {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int t = Integer.parseInt(br.readLine().trim());
        while (t-- > 0) {
            String inputLine[] = br.readLine().trim().split(" ");
            long n = inputLine.length;
            long arr[] = new long[(int)(n)];

            for (int i = 0; i < n; i++) {
                arr[i] = Long.parseLong(inputLine[i]);
            }

            Solution obj = new Solution();
            long answer[] = obj.findElements(arr);
            long sz = answer.length;

            StringBuilder output = new StringBuilder();
            for (int i = 0; i < sz; i++) output.append(answer[i] + " ");
            System.out.println(output);
        
System.out.println("~");
}
    }
}
class Solution {
    public long[] findElements(long arr[]) {
        int n=arr.length;
        if(n<=2)
        return new long[0];
        Arrays.sort(arr);
        return Arrays.copyOf(arr,n-2);
        
        // Your code goes here
    }
}