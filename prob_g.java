// ICPC 2016 Problem-G Vampire Number

import java.util.Scanner;
import java.util.Arrays ;

// import java.InputMismatchException;

class prob_g {

    static int int_pow(int base, double exp) {
        double d_base = (double)base ;
        return (int)(Math.pow(d_base, exp)) ;
    }


    static String sort_str(String s) {
        char[] c_ary = s.toCharArray() ;
        Arrays.sort(c_ary) ;
        String sorted = new String(c_ary) ;
        return sorted ;
    }

    static boolean check_combination(String n_sorted, int x, int y) {
        String x_str = String.valueOf(x) ;
        String y_str = String.valueOf(y) ;
        String xy_sorted = sort_str(x_str+y_str) ;

        if (n_sorted.equals(xy_sorted)) return true ;
        else {
            return false ;
        }
    }

    static boolean is_vampire(int n) {
        String n_str = String.valueOf(n) ;
        String n_str_sorted = sort_str(n_str) ;

        int n_len = n_str.length() ;
        if (n_len < 3 || n_len % 2 != 0) return false ;
        int low_limit = int_pow(10, (n_len / 2 - 1)) ;
        int high_limit = int_pow(n, 0.5) ;
        int high_limit_y = low_limit * 10 ;

        for (int x = low_limit; x <= high_limit; x++) {
            if (n % x != 0) continue ;
            int y = n / x ;
            if (y >= high_limit_y) continue ;
            if (x % 10 == 0 && y % 10 == 0) continue ;
            if (check_combination(n_str_sorted, x, y) == false) continue ;
            System.out.printf("%d=%d*%d\n", n, x, y) ;
            return true ;
        }

        return false ;
    }

    static void search_vampire(int low, int high) {
        int total = 0 ;

        for (int i=low; i<=high; i++) {
            if (is_vampire(i)) total += 1 ;
        }

        if (total == 0) System.out.println("NONE") ;
    }

    public static void main(String args[]) {
        Scanner scanner = new Scanner(System.in) ;
        String s = scanner.nextLine() ;

        int test_count ;
        test_count = Integer.parseInt(s) ;
/*
	try {
            test_count = Integer.parseInt(s) ;
	} catch (NumberFormatException e) {
            System.out.println(s+" can not be converted to Integer: "+e) ;
            scanner.close() ;
            return ;
        }
*/


        for (int i=0; i<test_count; i++) {
            System.out.printf("Case %d:\n", i+1) ;
            s = scanner.nextLine() ;
            String num[] = s.split(" ", 0) ;

            search_vampire(Integer.parseInt(num[0]), Integer.parseInt(num[1])) ;
        }

        scanner.close() ;
    }
}
