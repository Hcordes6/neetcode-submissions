class Solution {
    public int evalRPN(String[] tokens) {
        Stack<String> stack = new Stack<>();
        int sum = 0;
        for(int i = 0; i < tokens.length; i++) {
            if (tokens[i].equals("+") || tokens[i].equals("-") || tokens[i].equals("*") || tokens[i].equals("/")) {
                int second = Integer.parseInt(stack.pop());
                int first = Integer.parseInt(stack.pop());
                int itemPush = 0;
                System.out.println("in");
                if(tokens[i].equals("+")) {
                    itemPush = first + second;
                }
                if(tokens[i].equals("-")) {
                    itemPush = first - second;
                }
                if(tokens[i].equals("*")) {
                    itemPush = first * second;
                }
                if(tokens[i].equals("/")) {
                    itemPush = first / second;
                }
                stack.push(itemPush + "");
            } else {
                stack.push(tokens[i]);
            }
            System.out.println(stack.toString());
            

        }
        return Integer.parseInt(stack.peek());
    }
}
