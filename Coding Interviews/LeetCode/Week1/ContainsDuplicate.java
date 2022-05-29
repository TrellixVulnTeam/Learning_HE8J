import java.util.HashMap;

class ContainsDuplicate {

    public static boolean containsDuplicate(int[] nums) {
        HashMap<Integer, Integer> table = new HashMap<>();
        for(int i = 0; i < nums.length; i ++) {
            int n = nums[i];
            if (table.containsKey(n)) {
                return true;
            }
            table.put(n,1);
        }
        return false;
    }

    public static void main(String[] args) {
        int[] list = new int[]{1,2,3,4};
        System.out.println(containsDuplicate(list));
    }
}