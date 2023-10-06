def xorcount():
    """ 
    Only 1 digit at the time. First decimal and then hexadecimal
    so the program can perform a XOR-operation on each pair 
    before adding it to a list

    """

    d = []
    h = []
    x = []
    try:
        while len(d) !=(16):  
            _ = int(input('Enter \033[1m\033[94mdec \033[0m: '))
            d.append(_)
        while len(h) !=(16):               
            _ = int(input('Enter \033[1m\033[92mhex \033[0m: '),16)
            h.append(_)
        for i in range(0, len(d)):
            _ = (d[i]^h[i])
            _ = format(_, 'x')
            _ = _.upper()
            x.append(_)
    except ValueError: print("\N{Duck} says: Read documentation")  
    else:
        _ = ' '.join(x)
        print(f'\033[95m \033[92m\N{Duck} says: XOR-operator finished: \033[0m')
        print(f'\033[1m {_} \033[0m')


# xorcount()
