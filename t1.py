num = int(input("Coloque um número: "))

if num < 255:
    num_binario = 0
if num >= 255:
    num = num - 255
    num_binario = 1
    num_binario = str(num_binario)

if num < 128:
    num_binario = str(num_binario) + "0"
if num >= 128:
    num = num - 128
    num_binario = str(num_binario)+"1"

if num < 64:
    num_binario = str(num_binario) + "0"
if num >= 64:
    num = num - 64
    num_binario = str(num_binario)+"1"

if num < 32:
    num_binario = str(num_binario) + "0"
if num >= 32:
    num = num - 32
    num_binario = str(num_binario) + "1"

if num < 16:
    num_binario = str(num_binario) + "0"
if num >= 16:
    num = num - 16
    num_binario = str(num_binario) + "1"

if num < 8:
    num_binario = str(num_binario) + "0"
if num >= 8:
    num = num - 8
    num_binario = str(num_binario) + "1"

if num < 4:
    num_binario = str(num_binario) + "0"
if num >= 4:
    num = num - 4
    num_binario = str(num_binario) + "1"

if num < 2:
    num_binario = str(num_binario) + "0"
if num >= 2:
    num = num - 2
    num_binario = str(num_binario) + "1"

if num < 1:
    num_binario = str(num_binario) + "0"
if num >= 1:
    num = num - 1
    num_binario = str(num_binario) + "1"

print(num_binario)