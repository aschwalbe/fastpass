#!/usr/bin/env python3

'''
Name: Austin
Date: 2/23/2025
Project: CLI-based password generator
'''

import random
import sys
import argparse

# class for options
class options:
    characters = 15
    complexity = "l"
    minimize_output = False

# class for colors
### class of colors
class colors:
    header = '\033[95m'
    blue = '\033[94m'
    cyan = '\033[96m'
    green = '\033[92m'
    yellow = '\033[93m'
    red = '\033[91m'
    clear = '\033[0m'
    bold = '\033[1m'
    underline = '\033[4m'

# class for messages
class messages:

    # print green for success
    def Success(message):
        if (options.minimize_output == False):
            print(colors.green + "[*]  " + message + colors.clear)
    
    # print blue for info
    def Info(message):
        if (options.minimize_output == False):
            print(colors.blue + "[*]  " + message + colors.clear)

    # print red for error
    def Error(message):
        if (options.minimize_output == False):
            print(colors.red + "[ERROR]  " + message + colors.clear)

# lists of characters
lowercase = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
uppercase = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
special = ['%', '^', '&', '*', '!', '(', '-', '_']

# generate a password
# default: 8 characters, complexity on
def GenPass():

    # set initial variables
    characters = []
    password = ""

    # characters that will be in password
    # based on complexity
    if "l" in options.complexity: characters += lowercase
    if "u" in options.complexity: characters += uppercase
    if "n" in options.complexity: characters += numbers
    if "s" in options.complexity: characters += special

    # create the password
    for i in range(0, options.characters):
         rand = random.randint(0, len(characters)-1)
         password += characters[rand]

    # perform final check to meet complexity requirements
    check_pass = False
    password_new = [char for char in password]
    password = password_new
    while (not check_pass):

        # variables that will count characters
        num_l = 0
        num_u = 0
        num_n = 0
        num_s = 0

        # pick a random place that the new character (if added)
        # will be in
        rand = random.randint(0, len(password)-1)

        # count each type of character in the password
        for char in password:
            if char in lowercase: num_l += 1
            if char in uppercase: num_u += 1
            if char in numbers: num_n += 1
            if char in special: num_s += 1

        # if there is no lowercase character,
        # add a random lowercase character in a random place
        # and re-check password
        if (num_l == 0 and "l" in options.complexity):
            
            rand2 = random.randint(0, len(lowercase)-1)
            password[rand] = lowercase[rand2]
            continue

        # if there is no upperecase character,
        # add a random upperecase character in a random place
        # and re-check password
        elif (num_u == 0 and "u" in options.complexity):
            
            rand2 = random.randint(0, len(uppercase)-1)
            password[rand] = uppercase[rand2]
            continue

        # if there is no number,
        # add a random number in a random place
        # and re-check password
        elif (num_n == 0 and "n" in options.complexity):
            
            rand2 = random.randint(0, len(numbers)-1)
            password[rand] = numbers[rand2]
            continue

        # if there is no special character,
        # add a random special character in a random place
        # and re-check password
        elif (num_s == 0 and "s" in options.complexity):
            
            rand2 = random.randint(0, len(special)-1)
            password[rand] = special[rand2]
            continue

        # if everything passes, generate the password
        else: check_pass = True

    # re-create the password
    password_new = ""
    for char in password:
        password_new += char

    messages.Success("Password successfully created!")

    # return the password
    return password_new

###################################################################
#########################   DRIVER CODE   #########################
###################################################################


# parse input and check for anything invalid
# -n: Int flag, defines how many characters long the password will be
# -c: String flag, defines what types of characters will be used in the password
# -m: Boolean flag, enables minimial output mode when used
parser = argparse.ArgumentParser(description="Process user input with specific flags.")
parser.add_argument("-n", type=int, help="Length of characters (must be between 8-100)")
parser.add_argument("-c", type=str, help="Characters used (must include at least one of the following: l, u, n, s)")
parser.add_argument("-m", action="store_true", help="Minimizes output (i.e. only prints the password, nothing else)")

# parse arguments
args, unknown = parser.parse_known_args()

# parse invalid flags and unexpected arguments
if unknown:
    invalid_flags = [arg for arg in unknown if arg.startswith("-")]
    if invalid_flags:
        print(colors.red + f"[ERROR]  Invalid flags detected: {', '.join(invalid_flags)}" + colors.clear)
        sys.exit(1)
    print(colors.red + f"[ERROR]  Unexpected arguments: {', '.join(unknown)}" + colors.clear)
    sys.exit(1)

# parse -m
if args.m:
    options.minimize_output = True

# print header if minimal is not active
if not options.minimize_output:
    print("   ____ ____ ____ ____ ____ ____ ____ ____")
    print("  /___// . // __//_ _// . // . // __// __/")
    print(" /__/ /   //__ / / / / __//   //__ //__ /")
    print("/_/  /_/_//___/ /_/ /_/  /_/_//___//___/\n")
    print("      v1.1.0 by Austin Schwalbe\n")

# parse -n
if args.n is not None:
    if not 8 <= args.n <= 100:
        messages.Error("-n must be between 8 and 100")
        sys.exit(1)
    else:
        options.characters = args.n
    messages.Info("Setting password length to {} characters".format(options.characters))
else:
    messages.Info("Using default password length (15 characters)")

# parse -c
if args.c is not None:
    if (not any(char in args.c for char in "luns") or any(char in args.c for char in args.c if char not in "luns")):
        messages.Error("-c must contain at least one of l, u, n, or s")
        sys.exit(1)
    options.complexity = args.c
    types = ""
    if ("l" in options.complexity): types += "lowercase, "
    if ("u" in options.complexity): types += "uppercase, "
    if ("n" in options.complexity): types += "numbers, "
    if ("s" in options.complexity): types += "special, "
    if (options.complexity == "luns"): types = "all, "
    types = types.strip()[:-1]
    messages.Info("Setting character types to {}".format(types))
else:
    messages.Info("Using default password complexity (all lowercase)")

# generate a password
print(GenPass())
