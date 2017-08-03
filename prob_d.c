//    2016 ICPC at UCSY
//    Problem-D: Bakery Delivery Scheduler

#include <glib.h>
#include <stdlib.h>
#include <glib/gprintf.h>
#define INBUF_SIZE 10000
char in_buf[INBUF_SIZE] ;


#define MIN_ADDRESS (0)
#define MAX_ADDRESS (200)

struct test_case {
	gint min_address ;
	gint max_address ;
	gint shop_address ;
} ;

struct test_case *parse_tc(FILE *f) {
	#define END_MARK (-999)
	struct test_case *tc ;
//	gchar **next_token, **tokens ;

	tc = g_new0(struct test_case,1) ;
	if (NULL == tc) return tc ;

	tc->min_address = MAX_ADDRESS + 1 ;
	tc->max_address = MIN_ADDRESS - 1 ;

	while (1) {
		int cust_address ;

		if (NULL == fgets(in_buf, sizeof(in_buf), f)) {
			printf("input read error\n") ;
			g_free (tc) ;
			return NULL ;
		}

		cust_address = (gint)strtoul(in_buf, NULL, 10) ;
		if (cust_address == END_MARK) break ;

		if (cust_address > tc->max_address) tc->max_address = cust_address;
		if (cust_address < tc->min_address) tc->min_address = cust_address;
	}

	if (NULL == fgets(in_buf, sizeof(in_buf), f)) {
		printf("input read error\n") ;
		g_free (tc) ;
		return NULL ;
	}

	tc->shop_address = (gint)strtoul(in_buf, NULL, 10) ;

	return tc ;
}

int exec_test(FILE *f)
{
	struct test_case *tc ;
	if (NULL == (tc = parse_tc(f))) {
		return -1 ;
	}

	if (tc->shop_address < tc->min_address) {
		printf("Upword_First\n") ;
		printf("%d\n", tc->max_address - tc->shop_address) ;
	}
	else if (tc->shop_address > tc->max_address) {
		printf("Downword_First\n") ;
		printf("%d\n", tc->shop_address - tc->min_address) ;
	}
	else {
		gint low_dist, high_dist ;
		low_dist = tc->shop_address - tc->min_address ;
		high_dist = tc->max_address - tc->shop_address ;

		if (low_dist > high_dist) {
			printf("Upword_First\n") ;
			printf("%d\n", high_dist*2 + low_dist) ;
		}
		else {
			printf("Downword_First\n") ;
			printf("%d\n", low_dist*2 + high_dist) ;
		}
	}

	g_free(tc) ;
	return 0 ;
}

int main(int argc, char *argv[])
{
	FILE *f ;
	unsigned long i,t ;

	if (NULL == fgets(in_buf, sizeof(in_buf), stdin)) {
		printf("can not read from stdin\n") ;
		return -1 ;
	}

	t = strtoul(in_buf, NULL, 10) ;

	for (i=1 ; i<=t; i++) {
		if (exec_test(stdin)) {
			return -1 ;
		}
	}

	return 0 ;
}
