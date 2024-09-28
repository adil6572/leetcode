class Solution {
    public int missingNumber(int[] nums) {

       int xorAll=0;
       int xorArr=0;

        for (int i=1;i<=nums.length;i++){
            xorAll =xorAll^i ;
        }
     for (int i=0;i<nums.length;i++){
            xorAll =xorAll^nums[i] ;
        }
        return xorAll^xorArr;
    }
}