import os
import sys
import re
#print('Hello')

#print(sys.argv[1])
#print(sys.argv[2])
#print(sys.argv[3])
#print(sys.argv[4])

x = len(sys.argv)

if x > 1:
    if sys.argv[1] == '--help':
        print("That is help message for this script")
    if sys.argv[1] == "path":
            print("Please input path to file\nex: /home/user/file.txt")

    print('Arguments entered' + str(sys.argv[1:]))
else:
    print('Options  not provided\nPlease use --help or -h to get options for this script')

# os.system("ls -l")
