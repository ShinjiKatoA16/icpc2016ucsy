//
// prototype of code jam program
//

#include <glib.h>
#include <stdlib.h>
#include <glib/gprintf.h>
#define INBUF_SIZE 10000
char in_buf[INBUF_SIZE] ;

struct test_case {
	guint64 x ;
	guint64 y ;
} ;

struct test_case *parse_tc(FILE *f) {
	struct test_case *tc ;
	gchar **next_token, **tokens ;

	tc = g_new0(struct test_case,1) ;
	if (NULL == tc) return tc ;

	if (NULL == fgets(in_buf, sizeof(in_buf), f)) {
		printf("File read error in test case\n") ;
		g_free (tc) ;
		return NULL ;
	}

	next_token = tokens = g_strsplit(in_buf," ",-1) ;
	if (NULL == tokens) {
		printf ("strsplit failed\n") ;
		g_free (tc) ;
		return NULL ;
	}
	tc->x = (guint64)strtoul(*next_token++,NULL,10) ;
	tc->y = (guint64)strtoul(*next_token++,NULL,10) ;

	g_strfreev(tokens) ;

	return tc ;
}

int exec_test(FILE *f)
{
	struct test_case *tc ;
	if (NULL == (tc = parse_tc(f))) {
		return -1 ;
	}

	printf("X: %lu  Y: %lu\n",tc->x, tc->y) ;
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
		g_printf("Case %lu: ", i) ;
		if (exec_test(stdin)) {
			return -1 ;
		}
	}

	return 0 ;
}
