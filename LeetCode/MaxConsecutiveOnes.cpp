
// Problem Link:  https://leetcode.com/problems/max-consecutive-ones/

class Solution {
public:
    int findMaxConsecutiveOnes(vector<int>& nums) {
        int len =0;
        int max=0;
        
        for(int i:nums){
            if(i==1){
                len++;
                if(len>max){
                    max=len;
                }
            }
            else{
                len=0;
            }
        }
        return max;
    }
};
