public class BinaryToDecimal {
    public static int binaryToDecimal(String binaryString) {
        int decimal = 0;
        int power = 0;
        for (int i = binaryString.length() - 1; i >= 0; i--) {
            if (binaryString.charAt(i) == '1') {
                decimal += Math.pow(2, power);
            } else if (binaryString.charAt(i) != '0') {
                throw new IllegalArgumentException("Invalid binary string.");
            }
            power++;
        }
        return decimal;
    }

    public static void main(String[] args) {
        String binaryString = "101101";
        int decimal = binaryToDecimal(binaryString);
        System.out.println("Decimal equivalent: " + decimal);
    }
}
