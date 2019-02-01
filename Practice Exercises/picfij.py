# Famous "Picas & Fijas" game against the computer.
# The goal is to guess the number (it means, "Fijas" : 4). The
# exact number must be matched in order to win; the "Picas" number acts as a
# hint for the game. "Picas" number indicates how many digits match, but are in
# different position.
import random

# Loops flag
win = False
# Random 4-digit number without repeated digits.
randSet = random.sample(range(0,9),4)
cpuNum = []
for n in randSet:
    cpuNum.append(str(n))
usrNum = None
while not win:
    prevNum = usrNum
    usrNum = input('Insert a 4-digit number, please (to quit, enter end): ')
    if usrNum == 'end':
        print('You decided to quit...')
        print('The last number you typed in was:',prevNum)
        print('The cpu number was:',cpuNum)
        break # The game finishes
    # Number of digits that are equal and are in the same position.
    fij = len( [rep for rep in cpuNum if rep in usrNum and cpuNum.index(rep)==usrNum.index(rep)] )
    # Number of digits that are equal but are in a different position.
    pic = len( [rep for rep in cpuNum if rep in usrNum and cpuNum.index(rep)!=usrNum.index(rep)] )
    print('Fijas:', fij)
    print('Picas:',pic)
    # Ends if user guess the number
    if fij == 4:
        win = True
        print('CONGRATULATIONS!')
print('see ya!')
