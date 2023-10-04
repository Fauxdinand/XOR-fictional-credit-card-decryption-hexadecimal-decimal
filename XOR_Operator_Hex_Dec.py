def xorcount():
    """ 
    Only 1 digit at the time. First decimal and then hexadecimal
    so the program can perform a XOR-operation on each pair 
    before adding it to a list
    
    """
    count=0 
    deci=0
    hexa=0
    hexalist = []
    while count !=(16):
        try:
            deci = int(input('Enter dec: '))
            hexa = int(input('Enter hex: '), 16)
            xor = ((deci)^(hexa))
            noprefix = int(xor)
            hexalist.append(noprefix)
            count +=1
        except ValueError:
            print("\N{Duck} says: Read documentation")

        else:
            print(f'\033[95m \033[92m The duck says \N{Duck}: "XOR-operator finished: "\033[0m')
            print(f'\033[1m {hexalist} \033[0m')

xorcount()
