def xorcount():
    count=0 
    deci=0
    hexa=0
    hexalist = []
    while count !=(16):
        deci = int(input('Enter dec: '))
        hexa = int(input('Enter hex: '), 16)
        xor = ((deci)^(hexa))
        noprefix = int(xor)
        hexalist.append(noprefix)
        count +=1
    else:
         print(f'\033[95m \033[92m XOR-operator finished:\033[0m')
         print(f'\033[1m {hexalist} \033[0m')

xorcount()
