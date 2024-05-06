# python script.py result.txt


def myfn(*args, **kwargs):
    print(args[0])
    print(args[1])
    print(args[2])
    print(list(args))
    print(kwargs["one"])
    print(kwargs["two"])
    print(kwargs["three"])


# myfn(1, 2, 3, one="a", two="b", three="c")


import sys


# main(int argc, char** argv) # in c


print("filename: {sys.argv[0]}")  # filename
print(sys.argv[1])

filename = sys.argv[1]
message = sys.argv[2]

with open(filename, "w+") as f:
    f.write(message)


print(sys.argv)


#  For optional Args (opargs) we need flags
###############################################################################################
import getopt

filename = "text.txt"
message = "dummy"
# what kind of  optional args we need to accept?
opts, args = getopt.getopt(
    sys.argv[1:], "f:m", ["filename", "message"]
)  # what we take as input string: everything after argv[0]
# f:m:t
# (everything except first one, string: what are we waiting for)
# : means we are expecting string after the text filename after `m` and message after m
# but nothing after t

print(opts)
print(args)

for opt, arg in opts:
    if opt == "-f":
        filename = arg
    if opt == "-m":
        message = arg


with open(filename, "w+") as f:
    f.write(message)


# `python 09_args_parser.py -f mainq1.py -m testing1`
