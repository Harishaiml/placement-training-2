class Solution {
    public int searchInsert(int[] nums, int target) {
        int le=0;
        int  ri=nums.length-1;
        while (le<=ri){
            int mid =le+(ri-le)/2;
            if (nums[mid]==target){
                return mid;
            }else if (nums[mid]>target){
                ri=mid-1;
            }else{
                le=mid+1;
            }
        }
        return le;
    }
}
