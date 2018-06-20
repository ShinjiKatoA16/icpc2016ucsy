// ICPC 2016 Problem-D Delivery Schedule

import java.util.Scanner;


class prob_d {

    //static int MIN_ADDR = 0 ;
    //static int MAX_ADDR = 200 ;
    static int MIN_ADDR = Integer.MIN_VALUE ;
    static int MAX_ADDR = Integer.MAX_VALUE ;

    static void solve(Scanner sc) {
        int max_addr = MIN_ADDR ;
        int min_addr = MAX_ADDR ;

        while (true) {
            int addr = sc.nextInt() ;
            if (addr == -999) break ;
            if (addr < MIN_ADDR || addr > MAX_ADDR) {
                System.err.printf("Invalid input: %d\n", addr) ;
                return ;
            }

            if (addr < min_addr) min_addr = addr ;
            if (addr > max_addr) max_addr = addr ;
        }

        int shop_addr = sc.nextInt() ;
        int up_dist = max_addr - shop_addr ;
        int down_dist = shop_addr - min_addr ;

        if (shop_addr <= min_addr) {
            System.out.println("Upword_First") ;
            System.out.println(up_dist) ;
        }
        else if (shop_addr >= max_addr) {
            System.out.println("Downword_First") ;
            System.out.println(down_dist) ;
        }
        else {
            if (up_dist > down_dist) {
                System.out.println("Downword_First") ;
                System.out.println(down_dist*2 + up_dist) ;
            }
            else {
                System.out.println("Upword_First") ;
                System.out.println(up_dist*2 + down_dist) ;
            }
        }

        return ;
    }
            


    public static void main(String args[]) {
        Scanner sc = new Scanner(System.in) ;
        
        int test_count = sc.nextInt() ;

        for (int i=0; i<test_count; i++) {
            solve(sc) ;
        }

        sc.close() ;
    }
}
