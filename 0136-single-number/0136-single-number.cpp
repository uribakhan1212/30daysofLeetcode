class Solution {
public:
    int singleNumber(vector<int>& nums) {
        int temp = 0;
        int index = 0;
        int count = 0;
        int result = 0;
        for(int i = 0; i < nums.size(); i++)
        {
            temp = nums[index];
            if (temp == nums[i])
            {
                count+=1;
            }
            if((i == (nums.size() - 1))&& (count != 1))
            {
                i = -1;
                count = 0;
                index++;
            }
            else if((i == (nums.size() - 1))&& (count == 1))
            {
                result = temp;
                break;
            }
        }
        return result;
        
    }
};