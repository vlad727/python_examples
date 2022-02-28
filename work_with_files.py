# how to work with files

# path to file
list_names = "/home/vlad/PycharmProjects/pythonProject/names.txt"
# var for file (mode: read, write, append, r+ = read write mode), uncoding
names = open(list_names, mode='r', encoding='ascii')
# print file
# print(names.read())

# print lines from file (use strip for print without enter of the end line )
#for i in names:
#    print(i.strip())

# print only line with match 
for i in names:
    if "Adam" in i:
        print(i.strip())
