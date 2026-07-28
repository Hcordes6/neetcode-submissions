class Solution {
    public boolean isAnagram(String s, String t) {
        int[] bucketsS = new int[26];
        int[] bucketsT = new int[26];

        for(int i = 0; i < s.length(); i++) {
            int pos = (int) s.charAt(i) % 26;
            System.out.println(pos);
            bucketsS[pos] = bucketsS[pos] + 1;
            System.out.println(bucketsS[pos]);
        }
        for(int j = 0; j < t.length(); j++) {
            int pos = (int) t.charAt(j) % 26;
            bucketsT[pos]++;
        }
        for(int i = 0; i < 26; i++) {
            System.out.println(bucketsS[i] + " " + bucketsT[i]);
            if(bucketsS[i] != bucketsT[i]) return false;
        }
        return true;
    }
}
