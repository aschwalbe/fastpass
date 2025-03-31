# fastpass
A CLI-based password generator that allows you to create and customize passwords in seconds!

## Recent updates

### v1.1

Default passwords now align with the recommendations outlined in **NIST 800-63B, Rev 4**, including:
- A default character length of **15 characters** (minimum length of 8 characters)
- A default complexity of **none** (a.k.a. all lowercase)

### v1.0 (Release)

Fastpass available for download!

All passwords are generated 

## How to use

Usage: fastpass [options]

-n [8-100]: Defines length of password
-c [luns]: Defines character types of complexity (**l**owercase, **u**ppercase, **n**umbers, **s**pecial characters)
-m: Minimizes output (only prints password, nothing else)

## Examples

fastpass
- Prints a password using default length and complexity requirements outlined by NIST recommendations

fastpass -n 15 -c lu
- Prints a password with 15 characters using a combination of uppercase and lowercase letters

fastpass -n 9 -c n
- Prints a password with 9 characters using only numbers
