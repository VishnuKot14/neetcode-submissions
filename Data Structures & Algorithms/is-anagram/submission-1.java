class Solution {
    public boolean isAnagram(String s, String t) {
        if (s.length() != t.length()) {
            return false;
        }
        Hashtable<Character, Integer> sTable = new Hashtable<>();
        Hashtable<Character, Integer> tTable = new Hashtable<>();

        for (char c : s.toCharArray()) {
            sTable.put(c, sTable.getOrDefault(c, 0) + 1);
        }

        for (char c : t.toCharArray()) {
            tTable.put(c, tTable.getOrDefault(c, 0) + 1);
        }

        return sTable.equals(tTable);
    }
}
