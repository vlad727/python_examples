#!/usr/bin/python3
import os
import shutil
path = '/home/user'
print("Before coping file:")
print(os.listdir(path))
source = "/home/user/file.txt"

perms = os.stat(source).st_mode
print("File permisson mode:", perms, "\n")

destinationfile = "/home/user/file(copy).txt"

dest = shutil.copy(source, destinationfile)

print("After coping file:")
print(os.listdir(path))

perms = os.stat(destinationfile).st_mode
print("File permission mode:", perms)

print("Destination fileL", dest)
