/*
Given a string and a positive number k, find the longest substring of the string containing k distinct characters. 
If k is more than the total number of distinct characters in the string, return the whole string.
//https://medium.com/techie-delight/top-problems-on-sliding-window-technique-8e63f1e2b1fa
*/
import java.util.HashSet;
import java.util.Set;

class LongestSubstringWithKDistinctCharacters {
    public static final int CHAR_RANGE = 128;

    public static String findLongestSubstring(String input, int k) {
        if (input == null || input.isEmpty()) {
            return input;
        }

        int start = 0, end = 0;
        Set<Character> distinctChars = new HashSet<>();
        int[] charFrequency = new int[CHAR_RANGE];

        for (int left = 0, right = 0; right < input.length(); right++) {
            distinctChars.add(input.charAt(right));
            charFrequency[input.charAt(right)]++;

            while (distinctChars.size() > k) {
                if (--charFrequency[input.charAt(left)] == 0) {
                    distinctChars.remove(input.charAt(left));
                }
                left++;
            }

            if (end - start < right - left) {
                end = right;
                start = left;
            }
        }

        return input.substring(start, end + 1);
    }

    public static void main(String[] args) {
        String input = "abcbdbdbbdcdabd";
        int k = 2;
        System.out.println(findLongestSubstring(input, k));
    }
}
