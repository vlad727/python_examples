import sys

#print('Hello')

#print(sys.argv[1])
#print(sys.argv[2])
#print(sys.argv[3])
#print(sys.argv[4])

x = len(sys.argv)

if x > 1:
    print('Arguments entered' + sys.argv[:1])
else:
    print('Arguments no provided')
