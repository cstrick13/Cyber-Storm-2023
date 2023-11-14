###############################################################################
# Name: Colin Bumpass, CSC 442
# Date: September 19, 2023
# Desc: Upon receiving a txt file containing strings of binary, this file will 
#       determine if the binaries can be separated into 7 or 8 bits using the %
#       operator. 
#       
#       Then, it will tokenize the large string into groups of 7 or 8
#       bits and convert them to their corresponding ASCII characters. 
#       The ASCII characters will then be stored into an array until they are 
#       dumped into a string and returned and displayed in the terminal
#
#       Although this attempt is hardly optimal, I'd like to use the word "unique" 
# Credit: 
#        Lines 23 and 24 are straight from Trey's [Team Pteradactyl] first attempt
#        to make sure the inputted lines do not contain break statements. 
###############################################################################


import sys

# Credit: Trey Thomas 
binary_input = sys.stdin.read().strip()
binary_str = binary_input.replace("\r","").replace("\n", "").replace("\b","")

# Determine if binaries are 7-bit or 8-bit
if len(binary_str) % 8 == 0:
    mod = 8
else:
    mod = 7

# Duplicate the string, but place underscores to parse the groups of 7-bit or 8-bit 
newstring = ""
counter = 0
for i in binary_str:
    if counter % mod == 0 and counter != 0:
        newstring += "_"
    newstring += i
    counter +=1

# Now that the underscores are inserted, convert each 7-bit or 8-bit group of binaries
#     into their corresponding ASCII codes and store them in an array called characters
bits = ""
counter = 0
characters = []
while counter < len(newstring):
    bits = ""
    for i in newstring[counter:counter+mod+1]:
        if i == "_":
            counter +=1
            break
        else:
            bits += i
        counter +=1 

    # Convert to ASCII and store into array
    characters.append(chr(int(bits,2)))
    # Dump the contents of the array into a string
    result = ""
    for i in characters:
        result += i
# Return the string
sys.stdout.write(result + "\n")

