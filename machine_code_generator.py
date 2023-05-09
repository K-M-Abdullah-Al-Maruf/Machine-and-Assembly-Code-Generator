reg_mod_11_w_0 = {
    'al': '000',
    'cl': '001',
    'dl': '010',
    'bl': '011',
    'ah': '100',
    'ch': '101',
    'dh': '110',
    'bh': '111',
}
reg_mod_11_w_1 = {
    'ax': '000',
    'cx': '001',
    'dx': '010',
    'bx': '011',
    'sp': '100',
    'bp': '101',
    'si': '110',
    'di': '111',
}

r_m_mod_10 = {
    'bx+si': '000',
    'bx+di': '001',
    'bp+si': '010',
    'bp+di': '011',
    'si': '100',
    'di': '101',
    'bp': '110',
    'bx': '111',
}

r_m_mod_01 = {
    'bx+si': '000',
    'bx+di': '001',
    'bp+si': '010',
    'bp+di': '011',
    'si': '100',
    'di': '101',
    'bp': '110',
    'bx': '111',
}

r_m_mod_00 = {
    'bx+si': '000',
    'bx+di': '001',
    'bp+si': '010',
    'bp+di': '011',
    'si': '100',
    'di': '101',
    'd16': '110',
    'bx': '111',
}

binary_data = {
    '0': '0000',
    '1': '0001',
    '2': '0010',
    '3': '0011',
    '4': '0100',
    '5': '0101',
    '6': '0110',
    '7': '0111',
    '8': '1000',
    '9': '1001',
    'a': '1010',
    'b': '1011',
    'c': '1100',
    'd': '1101',
    'e': '1110',
    'f': '1111'
}

OPCODE = ''
D = ""
W = ""
MOD = ""
REG = ""
R_M = ""

BYTE_3 = ''
BYTE_4 = ''
source = ''
source_backup = ''
direct_address = ''

binary_code = ''


def print_all():
    print('\nOPCODE =', OPCODE)
    print("D =", D)
    print("W =", W)
    print("MOD =", MOD)
    print("REG =", REG)
    print("R_M =", R_M)
    print("BYTE 3 =", BYTE_3)
    print("BYTE 4 =", BYTE_4, end='\n\n')

    if BYTE_3 != '' and BYTE_4 != '':
        print("Offset is 16 bit")
    elif BYTE_3 != '' and BYTE_4 == '':
        print("Offset is 8 bit")
    elif BYTE_3 == '' and BYTE_4 == '':
        print("There is no offset")

    print()

    output = OPCODE + " " + D + " " + W + "  " + MOD + " " + REG + " " + R_M + " " + BYTE_3 + " " + BYTE_4
    print("OPCODE D W MOD REG R/M  BYTE-3  BYTE-4")
    print(output)


def displacement(x):
    print("x = ", x)
    global BYTE_3
    global BYTE_4
    if len(x) == 4:
        print(binary_data.get(x[1]))
        BYTE_4 = binary_data.get(x[0]) + binary_data.get(x[1])
        BYTE_3 = binary_data.get(x[2]) + binary_data.get(x[3])
    else:
        print(binary_data.get(x[0]))
        BYTE_3 = binary_data.get(x[0]) + binary_data.get(x[1])


def binary_in_4_segment(output_in_binary):
    output_in_binary_4_segment = ''
    for x in range(len(output_in_binary)):
        if (x + 1) % 4 == 0:
            output_in_binary_4_segment += output_in_binary[x] + " "
        else:
            output_in_binary_4_segment += output_in_binary[x]

    return output_in_binary_4_segment


def bin_to_hex(binary_4_segment):
    output_in_binary_4_segment_temp = binary_4_segment.split(' ')
    hex = ''
    binary_data_key = list(binary_data.keys())
    binary_data_value = list(binary_data.values())

    for x in range(len(output_in_binary_4_segment_temp) - 1):
        value = binary_data_value.index(output_in_binary_4_segment_temp[x])
        key = binary_data_key[value]

        if x == len(output_in_binary_4_segment_temp) - 2:
            hex += key.upper()
        elif (x + 1) % 2 == 0:
            hex += key.upper() + " "
        else:
            hex += key.upper()
    return hex


def assembly_code():
    global OPCODE
    global D
    global W
    global MOD
    global REG
    global R_M
    global BYTE_3
    global BYTE_4
    offset = ''

    for x in range(6):
        OPCODE += binary_code[x]

    D = binary_code[6]
    W = binary_code[7]
    MOD = binary_code[8] + binary_code[9]
    REG = binary_code[10] + binary_code[11] + binary_code[12]
    R_M = binary_code[13] + binary_code[14] + binary_code[15]

    if len(binary_code) == 24:
        for x in range(16, 24):
            BYTE_3 += binary_code[x]
        offset = bin_to_hex(binary_in_4_segment(BYTE_3))

    if len(binary_code) == 32:
        for x in range(16, 24):
            BYTE_3 += binary_code[x]
        for x in range(24, 32):
            BYTE_4 += binary_code[x]
        offset = bin_to_hex(binary_in_4_segment(BYTE_4))+bin_to_hex(binary_in_4_segment(BYTE_3))

    print("\nMachine code:")
    print(binary_in_4_segment(binary_code))

    print_all()

    if offset != "":
        print("\noffset = ", offset, 'h', sep='')

    print("\nRegister = REG + W")
    print("Addressing = MOD + R_M")


# --------------------------------------------------------------------
# --------------------------------------------------------------------


print("if inside a third bracket there is only a number then enter the number without bracket else enter everything along with bracket\n1)Assembly to machine\n2)Machine[HEX] to assembly\n3)Machine[Bin] to assembly")

inp = int(input())

if inp == 1:
    assembly_code = input().split(",")
    binary_code = input()
    OPCODE = binary_code
    print(assembly_code[0].lower())

    if assembly_code[0].lower() == "ax" or assembly_code[0].lower() == "bx" or assembly_code[0].lower() == "cx" or \
            assembly_code[0].lower() == "dx" or assembly_code[0].lower() == "ah" or assembly_code[0].lower() == "bh" or \
            assembly_code[0].lower() == "ch" or assembly_code[0].lower() == "dh" or assembly_code[0].lower() == "al" or \
            assembly_code[0].lower() == "bl" or assembly_code[0].lower() == "cl" or assembly_code[0].lower() == "dl"or assembly_code[0].lower() == "sp" or assembly_code[0].lower() == "bp" or assembly_code[0].lower() == "si"or assembly_code[0].lower() == "di":
        D = '1'
        if assembly_code[0][1].lower() == 'x' or assembly_code[0][1].lower() == 'p' or assembly_code[0][1].lower() == 'i':
            W = '1'
        else:
            W = '0'
    else:
        D = '0'
        print("assembly_code[1] =", assembly_code[1])
        if assembly_code[1].lower() == "ax" or assembly_code[1].lower() == "bx" or assembly_code[1].lower() == "cx" or \
                assembly_code[1].lower() == "dx" or assembly_code[1].lower() == "ah" or assembly_code[
            1].lower() == "bh" or assembly_code[1].lower() == "ch" or assembly_code[1].lower() == "dh" or assembly_code[
            1].lower() == "al" or assembly_code[1].lower() == "bl" or assembly_code[1].lower() == "cl" or assembly_code[
            1].lower() == "dl" or assembly_code[1].lower() == "sp" or assembly_code[1].lower() == "bp" or assembly_code[1].lower() == "si"or assembly_code[1].lower() == "di":
            if assembly_code[1][1].lower() == 'x' or assembly_code[1][1].lower() == 'p' or assembly_code[1][1].lower() == 'i':
                W = '1'
            else:
                W = '0'
        else:
            print("lol")
            print(assembly_code[1])
    if assembly_code[1][0] == '[':
        source_temp = assembly_code[1].split('[')
        source = (source_temp[1].split(']'))[0]

        source = source.split('+')

        if len(source) == 1:
            MOD = '00'
        elif len(source) == 2:
            if len(source[1]) <= 2:
               if source[1].lower() == 'si' or source[1].lower() == 'di':
                   MOD = '00'
               else:
                MOD = '01'
            else:
                MOD = '10'
        else:
            if len(source[2]) == 2:
                MOD = '01'
            else:
                MOD = '10'

    elif assembly_code[0][0] == '[':
        source_temp = assembly_code[0].split('[')
        source = (source_temp[1].split(']'))[0]
        source_backup = source
        source = source.split('+')
        if len(source) == 1:
            if source[0] != 'si' or source[0] != 'di' or source[0] != 'bx':
                direct_address = 'd16'
            MOD = '00'
        elif len(source) == 2:
            if len(source[1]) <= 2:
                if source[1].lower() == 'si' or source[1].lower() == 'di':
                    MOD = '00'
                else:
                    print("unga bunga")
                    MOD = '01'
            else:
                print("unga bunga2")
                MOD = '10'
        else:
            if len(source[2]) == 2:
                MOD = '01'
            else:
                print("unga bunga4")
                MOD = '10'

    elif (assembly_code[0].lower() == "ax" or assembly_code[0].lower() == "bx" or assembly_code[0].lower() == "cx" or
          assembly_code[0].lower() == "dx" or assembly_code[0].lower() == "ah" or assembly_code[0].lower() == "bh" or
          assembly_code[0].lower() == "ch" or assembly_code[0].lower() == "dh" or assembly_code[0].lower() == "al" or
          assembly_code[0].lower() == "bl" or assembly_code[0].lower() == "cl" or assembly_code[
              0].lower() == "dl"or assembly_code[0].lower() == "sp"or assembly_code[0].lower() == "bp"or assembly_code[0].lower() == "si"or assembly_code[0].lower() == "di") and (
            assembly_code[1].lower() == "ax" or assembly_code[1].lower() == "bx" or assembly_code[1].lower() == "cx" or
            assembly_code[1].lower() == "dx" or assembly_code[1].lower() == "ah" or assembly_code[1].lower() == "bh" or
            assembly_code[1].lower() == "ch" or assembly_code[1].lower() == "dh" or assembly_code[1].lower() == "al" or
            assembly_code[1].lower() == "bl" or assembly_code[1].lower() == "cl" or assembly_code[1].lower() == "dl"or assembly_code[1].lower() == "sp"or assembly_code[1].lower() == "bp"or assembly_code[1].lower() == "si"or assembly_code[1].lower() == "di"):
        MOD = '11'
    else:
        print("in else")
        MOD = '00'
        direct_address = 'd16'
        source = [assembly_code[1]]
        print("in else source = ",source)

    # work of reg
    if D == '0':
        if W == "0":
            REG = reg_mod_11_w_0.get(assembly_code[1].lower())
        else:
            REG = reg_mod_11_w_1.get(assembly_code[1].lower())
    else:
        if W == "0":
            REG = reg_mod_11_w_0.get(assembly_code[0].lower())
        else:
            REG = reg_mod_11_w_1.get(assembly_code[0].lower())
    # work of r/m
    if MOD == '11':
        if W == "0":
            REG = reg_mod_11_w_0.get(assembly_code[0])
        else:
            REG = reg_mod_11_w_1.get(assembly_code[0])
        if W == "0":
            R_M = reg_mod_11_w_0.get(assembly_code[1])
        else:
            print("yo")
            print(assembly_code[1])
            R_M = reg_mod_11_w_1.get(assembly_code[1])
    elif MOD == '00':
        if direct_address != '':
            print("source = ", source)
            R_M = r_m_mod_00.get(direct_address)
            print("r_m = ", R_M)
            displacement(source[0])
        elif len(source) == 2:
            print(source[0].lower()+source[1].lower())
            R_M = r_m_mod_00.get(source[0].lower()+"+"+source[1].lower())
            print("R\m = ", R_M )
        else:
            R_M = r_m_mod_00.get(source[0].lower())

    elif MOD == '01':
        if len(source) == 2:
            R_M = r_m_mod_01.get(source[0].lower())
            displacement(source[1])
        else:
            R_M = r_m_mod_01.get(source[0].lower()+"+"+source[1].lower())
            displacement(source[2])
    else:
        if len(source) == 2:
            print("source = ", source)
            R_M = r_m_mod_10.get(source[0].lower())
            displacement(source[1])
        else:
            R_M = r_m_mod_10.get(source[0].lower()+"+"+source[1].lower())
            displacement(source[2])

    print_all()



    output_in_binary = binary_code + D + W + MOD + REG + R_M + BYTE_3 + BYTE_4

    output_in_binary_4_segment = binary_in_4_segment(output_in_binary)
    print('\nOutput in 4 segment binary format:')
    print(output_in_binary_4_segment)

    binary_for_octal = output_in_binary_4_segment.replace(" ", "")
    print("\nBinary for octal format:")
    print(binary_for_octal)


    output_in_hex = bin_to_hex(output_in_binary_4_segment)

    print('\nOutput in hex format:')
    print(output_in_hex)

elif inp == 2:
    inp = input().lower()
    if inp[-1].lower() == 'h':
        hex_temp = inp.split(inp[-1])
        inp = hex_temp[0]

    hex_input = inp.split(' ')

    hex = ''

    if len(hex_input) == 1:
        hex = hex_input[0]
    else:
        for x in range(len(hex_input)):
            hex += hex_input[x]

    for x in range(len(hex)):
        binary_code += binary_data.get(hex[x])

    assembly_code()

else:
    binary_input = input().split(" ")

    if len(binary_input) == 1:
        binary_code = binary_input[0]
    else:
        for x in range(len(binary_input)):
            binary_code += binary_input[x]

    assembly_code()
