public class SimpleInterestCalculator {
    public static double calculateSimpleInterest(double principal, double rate, double time) {
        return (principal * rate * time) / 100;
    }

    public static void main(String[] args) {
        double principal = 1000;
        double rate = 5;
        double time = 2;
        double interest = calculateSimpleInterest(principal, rate, time);
        System.out.println("Simple interest: " + interest);
    }
}
