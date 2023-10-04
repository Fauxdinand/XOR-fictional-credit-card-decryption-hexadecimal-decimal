def xorcount():
    """ 
    Only 1 digit at the time. First decimal and then hexadecimal
    so the program can perform a XOR-operation on each pair 
    before adding it to a list

    """
    c=0 
    d=0
    h=0
    hl = []
    try:
        while c!=(16):
    
            d = int(input('Enter dec: '))
            h = int(input('Enter hex: '), 16)
            xr = ((d)^(h))
            np = format(xr, 'x')
            hs = np.upper()
            hl.append(hs)
            c +=1
    except ValueError:
            print("\N{Duck} says: Read documentation")

    else:
        l = ' '.join(hl)
        print(f'\033[95m \033[92m\N{Duck} says: XOR-operator finished: \033[0m')
        print(f'\033[1m {l} \033[0m')


# xorcount()
