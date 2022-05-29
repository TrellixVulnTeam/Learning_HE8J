import java.util.ArrayList;
import java.util.Collections;

public class SellStock {
    public static int maxProfit(int[] prices) {
        int temp_min = 9999999;
        int temp_max = -999999;
        int result = 0;
        int temp_result = 0;
        ArrayList<Integer> results = new ArrayList<>();
        for (int i = 0; i < prices.length; i ++) {
            if (prices[i] < temp_min) {
                temp_min = prices[i];
                //will store the latest temp result first
                temp_result = Math.max(result, temp_result);
                result = 0;
            }
            result = Math.max((prices[i] - temp_min), result);
        }
        //return Collections.max(results);
        return Math.max(result, temp_result);
    }

    public static void main(String[] args) {

        System.out.println(maxProfit(new int[]{7, 1, 5, 3, 6, 4}));
    }
}
