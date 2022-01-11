#!/bin/env python3

import sys

if len(sys.argv) > 2 or len(sys.argv) < 2:
    print('Usage:', sys.argv[0], '<output executable name>')
    sys.exit(1)

with open('Makefile', 'wt', encoding='utf-8') as makefile:
    makefile.write('CC=gcc\n')
    makefile.write('CFLAGS=\n')
    makefile.write('SRC=$(wildcard *.c)\n')
    makefile.write('OBJS=$(SRC:%.c=%.o)\n')
    makefile.write('TARGET=' + sys.argv[1] + '\n')
    makefile.write('\n')
    makefile.write('all: $(TARGET)\n')
    makefile.write('\n')
    makefile.write('$(TARGET): $(OBJS)\n')
    makefile.write('\t$(CC) -o $(TARGET) $(OBJS) $(CFLAGS)\n')
    makefile.write('\n')
    makefile.write('$(OBJS): $(SRC)\n')
    makefile.write('\t$(CC) -c $(SRC)\n')
    makefile.write('\n')
    makefile.write('clean:\n')
    makefile.write('\trm -f $(TARGET) $(OBJS)\n')

    makefile.close()

with open('main.c', 'wt', encoding='utf-8') as main:
    main.write('#include<stdio.h>\n')
    main.write('\n')
    main.write('int main(void){\n')
    main.write('\tprintf("Hello, World\\n");\n')
    main.write('\t\n')
    main.write('\treturn 0;\n')
    main.write('}\n')

    main.close()
