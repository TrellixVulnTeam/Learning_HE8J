import java.util.Stack;

class Solution {
    public boolean isValid(String s) {
        Stack<String> a = new Stack<>();
        char[] charArray  = s.toCharArray();
        for (char c : charArray) {
            a.push(String.valueOf(c));
        }

    }
}