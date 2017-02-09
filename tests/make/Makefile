LD=ld				# either ld or ld.gold
CC=gcc
CFLAGS=-Wall -Wextra

main: Makefile main.o
	$(LD) main.o -o $@
main.o: Makefile main.c
	$(CC) -c $(CFLAGS) main.c -o $@

clean:
	$(RM) main main.o
