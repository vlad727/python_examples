import os

# print current dir
cur_dir = os.getcwd()
print(cur_dir)

# list all files and dirs in current dir
contents = os.listdir()
print(contents)

# create new dir
os.mkdir("Temp")

# create sub dirs
os.makedirs("Temp/temp1/temp2/")

# delete empty dir
os.rmdir("Temp")

# rename dir 
os.rename("Temp","Temp11")
