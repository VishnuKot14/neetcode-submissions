class Solution {
    public boolean hasDuplicate(int[] nums) {
        Set<Integer> duplicates = new HashSet<>();
        for (int i = 0; i < nums.length; i++) {
            if (!duplicates.contains(nums[i])) {
                duplicates.add(nums[i]);
            } else {
                return true;
            }
        }

        return false;
    }
}