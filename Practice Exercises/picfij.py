# Famous "Picas y Fijas" game against the computer.
win = 'false'
cpuNum = '1234'
c1 = 0
c2 = 0
while win == 'false':
    pic = 0
    fij = 0
    c1 = 0
    c2 = 0
    usrNum = input('Insert a 4-digit number, please (to quit, enter 'end'): ')
    if usrNum == 'end':
        print('You decided to quit...')
        break # The game finishes
    for num_usr in usrNum:
        c1 = c1 + 1
        c2 = 0
        for cpu_num in cpuNum:
            c2 = c2 + 1
            if c1 == c2:
                if num_usr == cpu_num:
                    fij = fij + 1
            elif num_usr == cpu_num:
                pic = pic + 1
    print('Fijas:', fij)
    print('Picas:',pic)
    # Ends if user guess the number
    if fij == 4:
        win = 'true'
        print('CONGRATULATIONS!')
print('see ya!')
