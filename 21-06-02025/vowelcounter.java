public class VowelCounter {

    public static int countVowels(String str) {
        int count = 0;
        String vowels = "aeiouAEIOU";
        for (char c : str.toCharArray()) {
            if (vowels.indexOf(c) != -1) {
                count++;
            }
        }
        return count;
    }

    public static void main(String[] args) {
        java.util.Scanner scanner = new java.util.Scanner(System.in);
        System.out.print("Enter a string: ");
        String inputString = scanner.nextLine();
        int vowelCount = countVowels(inputString);
        System.out.println("Number of vowels: " + vowelCount);
        scanner.close();
    }
}
