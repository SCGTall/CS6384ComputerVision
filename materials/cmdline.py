# read command line arguments

import sys

# sys.argv is a list of arguments. len(sys.argv) is the number of arguments (+1)
# sys.argv[0] is the current script name
# sys.argv[1] is the first argument, etc

# this example insists on 2 arguments
if len(sys.argv) != 3 :
  print(sys.argv[0], "takes 2 arguments. Not ", len(sys.argv)-1)
  sys.exit()

first = sys.argv[1]
second = sys.argv[2]
print(sys.argv[0], "args are:", first, second)