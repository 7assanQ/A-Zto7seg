import os

os.system("") # enables ansi escape characters in terminal
class TC:
    BLA = '\033[90m'
    R = '\033[91m'
    G = '\033[92m'
    Y = '\033[93m'
    BLU = '\033[94m'
    M = '\033[95m'
    C = '\033[96m'
    W = '\033[97m'
    RESET = '\033[0m'

'''
To add more to dictionary_AZt07seg 

'character'    :   'binary representation in active low format'
    'X'        :                 'hgfedcba'
               |
    _          |         a
|       |      |     f       b
    _          |         g
|       |      |     e       c
    _       .  |         d       h
               |
_______________|__________________
    'A'        :     '10001000'
    'X'        :     'hgfedcba'
               |
    _          |         0
|       |      |     0       0
    _          |         0
|       |      |     0       0
    _       .  |         1       1    

    
also add the new character to the character_list string

'''

dictionary_AZt07seg = {
    'A' : '10001000',
    'b' : '10000011',
    'C' : '11000110',
    'd' : '10100001',
    'E' : '10000110',
    'F' : '10001110',
    'g' : '10010000',
    'H' : '10001001',
    'I' : '11111001',
    'j' : '11110010',
    'L' : '11000111',
    'n' : '11001000',
    'o' : '10100011',
    'P' : '10001100',
    'q' : '10001100',
    'r' : '10101111',
    'S' : '10010010',
    't' : '10000111',
    'U' : '11000001',
    'y' : '10011001',
    'Z' : '10100110',
    '0' : '11000000',
    '1' : '11111001',
    '2' : '10100100',
    '3' : '10110000',
    '4' : '10011001',
    '5' : '10010010',
    '6' : '10000010',
    '7' : '11111000',
    '8' : '10000000',
    '9' : '10010000',
    '.' : '01111111'
}

active = 'low'
character_list = 'A, b, C, d, E, F, g, H, I, j, L, n, o, P, q, r, S, t, U, y, Z, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, .'

def print_hex_shape(value):
    check_list = []
    check_current = dictionary_AZt07seg[value]
    hex_value = int(check_current, 2)

    print(TC.BLU + '\nThe value in hex is: ' + TC.W + hex(hex_value))

    if active == 'low':
        if check_current[7] == '0': check_list.append('_')
        else: check_list.append(' ')
        if check_current[6] == '0': check_list.append('|')
        else: check_list.append(' ')
        if check_current[5] == '0': check_list.append('|')
        else: check_list.append(' ')
        if check_current[4] == '0': check_list.append('_')
        else: check_list.append(' ')
        if check_current[3] == '0': check_list.append('|')
        else: check_list.append(' ')
        if check_current[2] == '0': check_list.append('|')
        else: check_list.append(' ')
        if check_current[1] == '0': check_list.append('_')
        else: check_list.append(' ')
        if check_current[0] == '0': check_list.append('.')
        else: check_list.append(' ')
    else: # if active high
        if check_current[7] == '1': check_list.append('_')
        else: check_list.append(' ')
        if check_current[6] == '1': check_list.append('|')
        else: check_list.append(' ')
        if check_current[5] == '1': check_list.append('|')
        else: check_list.append(' ')
        if check_current[4] == '1': check_list.append('_')
        else: check_list.append(' ')
        if check_current[3] == '1': check_list.append('|')
        else: check_list.append(' ')
        if check_current[2] == '1': check_list.append('|')
        else: check_list.append(' ')
        if check_current[1] == '1': check_list.append('_')
        else: check_list.append(' ')
        if check_current[0] == '1': check_list.append('.')
        else: check_list.append(' ')

    #print('      _ \n     |_|\n     |_|.')
    print(TC.Y + f'      {check_list[0]} \n     {check_list[5]}{check_list[6]}{check_list[1]}\n     {check_list[4]}{check_list[3]}{check_list[2]}{check_list[7]}')

def convert():
    print(TC.C + '\n----- Convert to 7-seg -----\n')
    print('Options: \n'+ TC.Y + character_list)
    user_input = input(TC.C + 'Enter here: ' + TC.G)

    if user_input in dictionary_AZt07seg.keys():
        print_hex_shape(user_input)
    else:
        if user_input.islower():
            if user_input.upper() in dictionary_AZt07seg.keys():
                print('\n' + TC.R + 'There is no ' + TC.G + user_input + TC.R + ' Do you mean uppercase ' + TC.G + user_input + TC.R + '?')
            else:   
                print('\n' + user_input + TC.R +  ' is not available')     
        elif user_input.isupper():
            if user_input.lower() in dictionary_AZt07seg.keys():
                print('\n' + TC.R + 'There is no ' + TC.G + user_input + TC.R + ' Do you mean lowercase ' + TC.G + user_input + TC.R + '?')
            else:   
                print('\n' + user_input + TC.R +  ' is not available')     
        else:   
            print('\n' + user_input + TC.R +  ' is not available')       

while(True):
    print(TC.C + '\n----- Control Menu -----\n')
    print(TC.G + 'First make sure to set all the 7-seg displays to (0xff if Active low) or (0x00 if Active high) on the FPGA board\n')
    print(TC.BLU + 'Active : '+ TC.W + active + '\n')

    try:
        user_input = int(input(TC.Y + '1)' + TC.M + 'Change Active low/high\n' + TC.Y + '2)' + TC.M + 'Convert to 7-seg\n' + TC.Y + '0)' + TC.Y + TC.R + 'Exit\n' + TC.C + 'options: ' + TC.Y + '0, 1, 2: ' + TC.G))
        match(user_input):
            case 0:
                print(TC.R + '\nExit the program...\n' + TC.RESET)
                break
            case 1:
                if active != 'high':
                    active = 'high'
                else:
                    active = 'low'    
            case 2:
                convert()
            case _:
                print(TC.R + 'Not a valid option...\n')  
    except:
        print(TC.R + 'Not a valid option...\n') 