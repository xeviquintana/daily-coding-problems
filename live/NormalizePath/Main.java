package NormalizePath;

/*
Normalize Path
Given a string s containing an absolute Unix-based directory path
write a program that normalizes this path using the following rules.

Input: "/usr/local//./../bin/."
Output: "/usr/bin"

Input: "/home/../.."
Output: "/"

Input: "/etc/system/../../home/user"
Output: "/home/user"
*/


import java.util.ArrayDeque;

public class Main {
	public static void main (String[] args) {
        System.out.println(normalizePath("/usr/local//./../bin/."));
        System.out.println(normalizePath("/home/../.."));
        System.out.println(normalizePath("/etc/system/../../home/user"));
    }
    
    private static String normalizePath(String path) {
        final String SEPARATOR = "/";
        String[] pathElements = path.split(SEPARATOR);
        ArrayDeque<String> deque = new ArrayDeque<>(pathElements.length);

        for(String element : pathElements) {
            if(element.equals("..")) {
                if (!deque.isEmpty())
                    deque.removeLast();
            }
            else if (!element.equals(".") && !element.isEmpty()) {
                deque.add(element);
            }
        }

        return SEPARATOR + String.join(SEPARATOR, deque);
    }
}
