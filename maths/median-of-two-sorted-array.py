class Solution {
public:
    double findMedianSortedArrays(vector<int>& nums1, vector<int>& nums2) {
        //For merging the arrays
        vector<int> ans;
        
        //For iterating in the arrays
        int i = 0;
        int m = 0;
        
        //both arrays are traversing simultaneously
        while(i < nums1.size() && m < nums2.size()){
            if(nums1[i] > nums2[m]){
                ans.push_back(nums2[m]);
                m++;
            }
            else{
                ans.push_back(nums1[i]);
                i++;
            }
        }
        
        //array 1 traversing if needed
        while(i < nums1.size()){
            ans.push_back(nums1[i]);
            i++;
        }
        
        //array 2 travering if needed
        while(m < nums2.size()){
            ans.push_back(nums2[m]);
            m++;
        }
        
        //now for median calculation
        int n = ans.size();
        
        //if n is odd
        if(n%2 != 0){
            return ans[n/2];
        }
        
        //if n is even
        else{
            int a = ans[n/2];
            int b = ans[(n/2) - 1];
            double res = (a+b)/2.0;
            return res;
        }
    }
};
