def xorcount():
    count=0 
    deci=0
    hexa=0
    hexalist = []
    while count !=(16):
        deci = int(input('Enter dec: '))
        hexa = int(input('Enter hex: '), 16)
        xor = ((deci)^(hexa))
        hexalist.append(hex(xor))
        count +=1
    else:
         print(hexalist)

xorcount()

