class Solution {
public:
    void moveZeroes(vector<int>& nums) {
        
       	vector<int>::iterator it;
        it = nums.begin();
        int count=0;
        if(nums.size()>1){
            for(int i=0;i<nums.size();i++){
                if(nums[i]==0){
                    count++;
                    nums.erase(it+i);
                    i--;
                }
        }
        while(count--){
            nums.push_back(0);
        }
        }
        
    }
};