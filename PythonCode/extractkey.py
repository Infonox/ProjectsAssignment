#!/usr/bin/env python
import sys
with open("../html/files/a-web/tid1input.txt", "r") as input:
        input_ = input.read().split(".\n")
        word = sys.argv[1]
        for i in input_:
            outcome = i.split()
            if word in outcome:
                testfile = open("../html/files/a-web/webanswer.txt", "w")
                testfile.write(i)
                testfile.close() 
f = open("../html/files/a-web/webanswer.txt", "r")
print(f.read())

