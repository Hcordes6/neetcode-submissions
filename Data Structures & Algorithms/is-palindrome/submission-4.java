class Solution {
    public boolean isPalindrome(String s) {
        String finalString = "";
        
        for(int i = 0; i < s.length(); i++) {
            if(Character.isLetterOrDigit(s.charAt(i))){
                finalString = finalString.concat(s.substring(i,i+1).toLowerCase());
            }
        }


        System.out.println(finalString);
        
        int i = 0;
        int j = finalString.length() - 1;
        while(i <= j) {
            if (finalString.length() == 1) {
                break;
            }
            if (finalString.charAt(i) != finalString.charAt(j)){
                return false;
            } 
            i++;
            j--;
        }
        return true;
    }

}