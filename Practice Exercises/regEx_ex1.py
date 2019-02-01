# Read through and parse a file with text and numbers.
# You will extract all the numbers in the file and compute the sum of the numbers.

# Any '.txt' file can be created and uploaded, and all numbers on it will be
# summed.
import re

# '+' is used in order to match at least 1 digit.
print( sum([ int(num) for num in re.findall('[0-9]+',open('text.txt').read()) ]) )
