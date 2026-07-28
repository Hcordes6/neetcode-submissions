class Solution {
    public int[] twoSum(int[] nums, int target) {
        HashMap<Integer, Integer> hashMap = new HashMap<>();
        int difference;
        int[] returnVals = new int[2];


        for(int i = 0; i < nums.length; i++) {
            difference = target - nums[i];
            hashMap.put(difference, i);
        }
        
        for(int j = 0; j < nums.length; j++) {
            if(hashMap.containsKey(nums[j])) {
                if(j < hashMap.get(nums[j])) {
                    returnVals[0] = j;
                    returnVals[1] = hashMap.get(nums[j]);
                    return returnVals;
                } else if (j > hashMap.get(nums[j])) {
                    returnVals[0] = hashMap.get(nums[j]);
                    returnVals[1] = j;
                    return returnVals;
                }
            }
            
        }
        return null;
        
    }
}

// if(hashMap.containsKey(difference)) {
//                 System.out.println("in loop");
//                 if(hashMap.get(difference) < j){
//                     returnVals[0] = hashMap.get(difference);
//                     returnVals[1] = j;
//                     return returnVals;
//                 } else if (hashMap.get(difference) > j){
//                     returnVals[1] = hashMap.get(difference);
//                     returnVals[0] = j;
//                     return returnVals;
//                 }
//                 System.out.println(hashMap.get(difference));
//             }
