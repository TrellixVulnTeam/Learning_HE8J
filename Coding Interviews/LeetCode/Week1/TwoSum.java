import java.util.ArrayList;
import java.util.Arrays;
import java.util.Scanner;
import java.util.HashMap;

// public class TwoSum {

//     public static int[] twoSum(ArrayList<Integer> nums, int target) {
//         for (int i = 0; i < nums.size(); i ++) {
//             int temp = target - nums.get(i);
//             if (nums.contains(temp)) {
//                 return new int[]{i, nums.indexOf(temp)};
        
//             }
//         }
//         return null;
//     }


    
// }

public class TwoSum {
    public static int[] twoSum(int[] numbers, int target) {
        
        HashMap<Integer,Integer> hash = new HashMap<Integer,Integer>();
        for(int i = 0; i < numbers.length; i++){

            Integer diff = target - numbers[i];
            if(hash.containsKey(diff)){
                return new int[]{hash.get(diff), i};
            }

            hash.put(numbers[i], i);

        }
        
        return null;
        
    }

    public static void main(String[] args) {
         Scanner sc = new Scanner(System.in);
         int N = sc.nextInt();

         int[] nums = new int[N];
         for (int i = 0; i < N; i ++) {
             nums[i] = sc.nextInt();
         }

         int target = sc.nextInt();

         sc.close();

         System.out.println(Arrays.toString(twoSum(nums, target)));
     }
}
