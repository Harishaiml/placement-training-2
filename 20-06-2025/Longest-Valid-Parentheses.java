class Solution_stack {
    public int longestValidParentheses(String s) {
        Stack<Integer> sk = new Stack<>();
        int start = 0;
        int result = 0;
        for (int i = 0;i < s.length(); i++) {
            if(s.charAt(i) == '(') {
                sk.push(i);
            } else {
                if (sk.empty()) {
                    start = i + 1;
                } else {
                    sk.pop();
                    result = Math.max(result, sk.isEmpty() ? i - start + 1 : i - sk.peek());
                }
            }
        }
        return result;

    }
}
