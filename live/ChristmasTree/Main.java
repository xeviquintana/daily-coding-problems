package ChristmasTree;

/*
Christmas Tree
Given an integer, n, write a program
that prints on the standard output an ASCII Christmas tree
made of spaces and stars with a height of n lines.

Input:
n = 4

Output:
   *
  ***
 *****
*******
*/

public class Main {
    public static void main (String[] args) {	
        printStars(4);
        printStars(-1);
    }
  
    private static void printStars(int n) {
        for (int i = 0; i < n; i++) {
            String lpad = " ".repeat(n - i - 1);
            String nStars = "*".repeat(2 * i + 1);
            System.out.println(lpad.concat(nStars));
        }
    }
}
