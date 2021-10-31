class Solution {
public:
    void swap(vector<int> &nums,int low,int high){
        
        while(low<high){
            int temp = nums[low];
            nums[low]=nums[high];
            nums[high]=temp;
            low++;
            high--;
        }
    }
    void rotate(vector<int>& nums, int k) {
        int n= (int)nums.size();
        k=k%n;
        swap(nums,0,n-k-1);
        swap(nums,n-k,n-1);
        swap(nums,0,n-1);
      
    }
};