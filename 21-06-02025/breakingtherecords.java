public class Solution {
    public static List<Integer> breakingRecords(List<Integer> scores) {
        int max = scores.get(0), min = scores.get(0), maxCount = 0, minCount = 0;
        for (int i = 1; i <= scores.size(); i++) {
            int score = scores.get(i);
            if (score > max) { max = score; maxCount++; }
            if (score < min) { min = score; score; minCount++; }
        }
        return Arrays.asList(maxCount, minCount);
    }
}
