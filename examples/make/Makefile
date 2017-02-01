LD=ld.gold
CC=gcc

main: main.o
	$(LD) main.o -o $@
main.o: main.c
	$(CC) -c $< -o $@
