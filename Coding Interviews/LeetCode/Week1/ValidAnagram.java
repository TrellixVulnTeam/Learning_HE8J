import java.util.HashMap;

class ValidAnagram {
    public HashMap<String, Integer> toHash (String s ) {
        HashMap<String, Integer> sMap = new HashMap<>();
        for (int i = 0; i < s.length(); i++ ) {
            String c = Character.toString(s.charAt(i));
            if (sMap.containsKey(c)) {
                sMap.put(c, sMap.get(c)+1);
            }
            else {
                sMap.put(c, 1);
            }
        }
        return sMap;
    }

    public boolean isAnagram(String s, String t) {
        HashMap<String, Integer> sMap =  toHash(s);
        HashMap<String, Integer> tMap =  toHash(t);
        return sMap.equals(tMap);
     }
}