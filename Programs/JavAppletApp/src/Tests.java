import java.util.Scanner;
import java.util.ArrayList;

public class Tests {
	static ArrayList<Long> visited = new ArrayList<Long>();
	
	public static void main(String[] args) {
		Scanner in = new Scanner(System.in);
		
		long num = in.nextLong();
		isHappy(num);
	}
	
	public static long sumOfSquares(long num) {
		if (num == 0) return 0;
		
		long digit = num % 10;
		
		return digit * digit + sumOfSquares(num / 10);
	}
	
	public static void isHappy(long num) {
		if (visited.contains(num)) {
			System.out.println("sad");
			return;
		}
		if (num == 1) {
			System.out.println("happy");
			return;
		}
		
		visited.add(num);
		
		isHappy(sumOfSquares(num));
	}
}