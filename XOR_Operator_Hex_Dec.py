
def xorcount():
    count=0 
    deci=0
    hexa=0
    while count !=(16):
        deci = int(input('Enter dec: '))
        hexa = int(input('Enter hex: '), 16)
        xor = ((deci)^(hexa))
        print(hex(xor))
        count +=1
    if count == (16):
         print('Finished! Remember to remove prefix 0x')

xorcount()

