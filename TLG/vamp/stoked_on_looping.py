#!/usr/bin/env python3

#importing libraries
#starting counter
vampcount = 0
draccount = 0

#reading dracula.txt as a file object
with open("dracula.txt") as dfile:
    # looping over the lines
    for line in dfile:
        line = line.lower()
        if "vampire" in line:
            vampcount +=1 # adding another to the vamp counter
            with open("vampy_lines.txt","a") as output_vamp:
                print(f"#{vampcount}: {line}", file=output_vamp)
            """with open("vampy_lines.txt","a") as output_vamp: # trying to reset each time I run
                print(f"#{vampcount}: {line}", file=output_vamp)"""
        if "dracula" in line:
            draccount += 1 # looking for the man himself
            with open("draccy_lines.txt","a") as output_drac:
                print(f"#{draccount}: {line}", file=output_drac)
print(f"Wow, only {vampcount} mentions of vampire in the whole book! Check out vampy_lines.txt for all the mentions and draccy_lines.txt for all mentions of the eponym.")
