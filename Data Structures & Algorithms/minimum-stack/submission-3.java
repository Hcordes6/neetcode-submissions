class MinStack {

    ArrayList<Integer> stack;
    int lastPointer;
    LinkedList<Integer> minStack;
    public MinStack() {
        stack = new ArrayList<>();
        lastPointer = -1;
        minStack = new LinkedList<>();
    }
    
    public void push(int val) {
        stack.add(val);
        lastPointer++;
        if (minStack.isEmpty() || val <= minStack.getLast()) {
            minStack.addLast(val);
        }
        System.out.println(stack.toString());
        System.out.println(minStack.toString());
    }
    
    public void pop() {
        int removed = stack.remove(lastPointer);
        if (removed == minStack.getLast()) {
            minStack.removeLast();
        }
        System.out.println(stack.toString());
        System.out.println(minStack.toString());
        lastPointer--;
    }
    
    public int top() {
        return stack.get(lastPointer);
    }
    
    public int getMin() {
        if (minStack.isEmpty()) {
            return 0;
        }
        return minStack.getLast();
    }
}
