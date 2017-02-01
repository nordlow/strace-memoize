LD=ld.gold
CC=gcc

main: Makefile main.o
	$(LD) main.o -o $@
main.o: Makefile main.c
	$(CC) -c -Wall -Wextra main.c -o $@
