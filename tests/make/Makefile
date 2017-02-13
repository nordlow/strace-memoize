LD=ld				# either ld or ld.gold
LDFLAGS=-lc

CC=gcc
CFLAGS=-Wall -Wextra -Wno-unused-parameter -Iinclude

main: Makefile main.o
	$(LD) $(LDFLAGS) main.o -o $@
main.o: Makefile main.c
	$(CC) -c $(CFLAGS) main.c -o $@

clean:
	$(RM) main main.o
