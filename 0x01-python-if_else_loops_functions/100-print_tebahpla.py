#!/usr/bin/python3
for chr in reversed(range(97, 123)):
    print("{:c}".format(chr if (chr % 2 == 0) else (chr - 32)), end='')
