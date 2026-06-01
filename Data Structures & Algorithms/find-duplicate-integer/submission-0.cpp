class Solution {
public:
    int findDuplicate(vector<int>& nums) {
        int n = nums.size();
        int* H = new int[n + 1]();  // Create array on heap, () initializes to 0
        
        for (int i = 0; i < n; i++) {
            H[nums[i]]++;
            if (H[nums[i]] > 1) {
                delete[] H;  // Clean up memory
                return nums[i];
            }
        }
        
        delete[] H;  // Clean up memory
        return -1;
    }
};

