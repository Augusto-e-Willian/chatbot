# Armazenar um número entre 0 e 255.por exemplo,o número 120.
numero=120

#subtraia o numero por 128, se o resultado da operação for 0 ou superior então o bit é 1
if (numero- 128) >=0:
    binario= "1"
    numero = numero - 128
else:
    binario =  "0"




#subtraia o numero por 64, se o resultado da operação for 0 ou superior então o bit é 1
if (numero- 64) >=0:
    binario=binario + "1"
    numero = numero - 64
else:
    binario= binario + "0"




#subtraia o numero por 32, se o resultado da operação for 0 ou superior então o bit é 1
if (numero- 32) >=0:
    binario=binario + "1"
    numero = numero - 32
else:
    binario = binario + "0"




#subtraia o numero por 16, se o resultado da operação for 0 ou superior então o bit é 1
if (numero- 16) >=0:
    binario=binario + "1"
    numero = numero - 16
else:
    binario= binario + "0"



#subtraia o numero por 8, se o resultado da operação for 0 ou superior então o bit é 1
if (numero- 8) >=0:
    binario=binario + "1"
    numero = numero - 8
else:
    binario= binario + "0"




#subtraia o numero por 4, se o resultado da operação for 0 ou superior então o bit é 1
if (numero- 4) >=0:
    binario=binario + "1"
    numero = numero - 4
else:
    binario = binario + "0"




#subtraia o numero por 2, se o resultado da operação for 0 ou superior então o bit é 1
if (numero- 2) >=0:
    binario=binario + "1"
    numero = numero - 2
else:
    binario= binario + "0"




#subtraia o numero por 1, se o resultado da operação for 0 ou superior então o bit é 1
if (numero- 1) >=0:
    binario=binario + "1"
    numero = numero - 1
else:
    binario = binario + "0"


print(numero)
print(binario)