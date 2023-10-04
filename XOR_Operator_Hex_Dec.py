
def xorcount():
    """ 
    Only 1 digits at the time. First decimal and then hexadecimal
    so the program can perform a XOR-operation on each pair 
    before adding it to a list

    """
    d=0
    h=0
    dl = []
    hl = []
    xl = []
    try:
        while len(dl) !=(16):  
            d = int(input('Enter \033[1m\033[94mdec \033[0m: '))
            dl.append(d)
        while len(hl) !=(16):               
            h = int(input('Enter \033[1m\033[92mhex \033[0m: '), 16)
            hl.append(h)
        for i in range(0, len(dl)):
            xi = (dl[i] ^ hl[i])
            xf = format(xi, 'x')
            xb = xf.upper()
            xl.append(xb)
    except ValueError:
            print("\N{Duck} says: Read documentation")
    else:
        xp = ' '.join(xl)
        print(f'\033[95m \033[92m\N{Duck} says: XOR-operator finished: \033[0m')
        print(f'\033[1m {xp} \033[0m')


xorcount()
