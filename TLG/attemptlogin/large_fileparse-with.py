#!/usr/bin/env python3

# defining the coutner for failed attempts
loginfail = 0
loginsuccess = 0

# open the file for reading
with open("/home/student/mycode/attemptlogin/keystone.common.wsgi") as kfile:
    # looping over the list of lines
    for line in kfile:
        # if this pattern appears
        if "- - - - -] Authorization failed" in line:
            loginfail += 1 # increasing fail counter
            failed_ip = line.split(" ")[-1]
        elif "-] Authorization failed" in line:
            loginsuccess += 1 # increasing success counter
            successful_ip = line.split(" ")[-1] 
print(f"The total number of failed log in attempts is {loginfail}. The attempts came from {failed_ip}")
print(f"The total number of successful log in attempts is {loginsuccess}. The user logged in from {successful_ip}")
