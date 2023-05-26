#!/usr/bin/env python3

# defining the coutner for failed attempts
loginfail = 0

# open the file for reading
keystone_file = open("/home/student/mycode/attemptlogin/keystone.common.wsgi","r")

# turning the file into a list in memory
keystone_file_lines = keystone_file.readlines()

# for my own edification here - printing this will look EXACTLY the same as the file itself
#print(keystone_file_lines)
# this should return just the first line
#print(keystone_file_lines[0])

# looping over the list of lines
for line in keystone_file_lines:
    # if this pattern appears
    if "- - - - -] Authorization failed" in line:
        loginfail += 1 # increasing the counter
print(f"The total number of failed log in attempts is {loginfail}.")
keystone_file.close() # close that file!
