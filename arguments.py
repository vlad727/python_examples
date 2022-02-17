import os
import sys

#print('Hello')

#print(sys.argv[1])
#print(sys.argv[2])
#print(sys.argv[3])
#print(sys.argv[4])

x = len(sys.argv)

if x > 1:
    if sys.argv[1] == '--help':
        print("That is help message for this script")
    print('Arguments entered' + str(sys.argv[1:]))
else:
    print('Arguments no provided')

os.system("ls -l")
