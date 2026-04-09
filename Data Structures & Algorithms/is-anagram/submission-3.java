class Solution {
    public boolean isAnagram(String s, String t) {
        if (s.length() != t.length()) {
            return false;
        }
        int[] sCharMap = new int[26];
        int[] tCharMap = new int[26];

        for (int i = 0; i < s.length(); i++) {
            sCharMap[s.charAt(i) - 'a']++;
            tCharMap[t.charAt(i) - 'a']++;
        }


        for (int i = 0; i < 26; i++) {
            if (sCharMap[i] != tCharMap[i]) {
                return false;
            }
        }
        return true;

    }
}
