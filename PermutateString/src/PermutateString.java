/*
 * This program contains the definition/description of a method (which you will write)
 * that generates all possible permutations of a string, and prints them out.
 * Further details of the method will be embedded in the comments above 
 * its prototype.
 *
 * Hint: Research Recursion
 */
public class PermutateString {
	/*
	 * All this main functions does is call 
	 * the printPermutatedString method.
	 * You should not edit the strings that
	 * are passed to the function, but you may
	 * edit the function calls to accomodate
	 * any chances that you might've made
	 * to the printPermutatedString method
	 */
	public static void main(String[] args) {
		//Some basic tests...
		//printPermutatedString(new StringBuffer("abc"), new StringBuffer(""));
//		printPermutatedString(new StringBuffer("abcd"), new StringBuffer(""));
		printPermutatedString(new StringBuffer("KewlKids"), new StringBuffer(""));
		
		
//		//Some Medium tests...
//		printPermutatedString(new StringBuffer("abcde"), new StringBuffer(""));
//		printPermutatedString(new StringBuffer("abcdef"), new StringBuffer(""));
//		
//		//Long test...
//		printPermutatedString(new StringBuffer("WickedCool"), new StringBuffer(""));
	}

	/*
	 * This is what you should code.
	 * (If you feel like you need to modify the method declaration in any way,
	 *  do so at your discretion, but be sure to accomodate the changes
	 *  that you’ve made below with the calls to this method in the main method above)
	 *  Your code will be evaluated individually, and we’ll try
	 *  to give you feed-back about what you did right or wrong.
	 * 
	 * This method should, given a string of characters,
	 * print out all of the permutations of all the characters in the string.
	 * (the “current” parameter is for recursion, which we recommend you research/look-up)
	 *
	 * E.G: Given a string with “abc”, this method should print out, on separate lines,
	 * abc, acb, cba, cab, bca, bac 
	 * In any order.
	 * 
	 * The strings passed to this method can be of any length, but we'll
	 * make it so that the function will terminate in a reasonable amount of
	 * time if it uses recursion.
	 * 
	 * (By the way, the StringBuffer behaves in the exact same way as a normal String object
	 *  but it provides certain methods that may be useful in coding a solution to the problem)
	 */
	public static void printPermutatedString(StringBuffer inventory, StringBuffer current) {
		//Base case -- check if the inventory is empty which means
		//we've used all of the characters to generate a full permutation
		//of the original set of characters
		if (inventory.length() == 0) {
			//Print out the permutation
			System.out.println(current);
		}
		else {
			//Otherwise, try all possible letter combinations
			for (int x = 0; x < inventory.length(); x++) {
				//First duplicate the inventory and the current permutation
				//that we're forming
				StringBuffer newInventory = new StringBuffer(inventory);
				StringBuffer newCurrent = new StringBuffer(current);
				
				//Remove from the inventory the character we're going to append
				//to the permutation we're currently forming
				newInventory.deleteCharAt(x);
				newCurrent.append(inventory.charAt(x));
				
				//Recurse
				printPermutatedString(newInventory, newCurrent);
			}
		}
	}
}