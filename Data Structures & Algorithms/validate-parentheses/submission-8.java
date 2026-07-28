class Solution {
    public boolean isValid(String s) {
        Stack<Character> stack = new Stack();
        boolean isValid = true;
        for(int i = 0; i < s.length(); i++) {
            char nextChar = s.charAt(i);
            if (nextChar == '(' || nextChar == '[' || nextChar == '{') {
                stack.push(nextChar);
            }
            else {
                if (stack.isEmpty()) {
                    return false;
                } else if((stack.peek().equals('(') && nextChar == ')') || 
                    (stack.peek().equals('[') && nextChar == ']') || 
                    (stack.peek().equals('{') && nextChar == '}')) {
                    stack.pop();
                }
                else {
                    return false;
                } 
            }
            
        }
        if (!stack.isEmpty()) return false;
        return isValid;
    }
}
