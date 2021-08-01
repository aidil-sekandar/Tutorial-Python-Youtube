print("""Sila pilih opersi:
1. +
2. -
3. ×
4. ÷""")
bilangan_operasi = 0

teruskan = input("Mahu teruskan? (Y/T) : ").upper()
print("")

while teruskan == "Y":

    operasi = int(input("Sila pilih operasi (1/2/3/4) : "))
    nombor1 = int(input("Nombor pertama = "))
    nombor2 = int(input("Nombor kedua = "))

    if operasi == 1:
        print(f"{nombor1} + {nombor2} = {nombor1 + nombor2}")
    elif operasi == 2:
        print(f"{nombor1} - {nombor2} = {nombor1 - nombor2}")
    elif operasi == 3:
        print(f"{nombor1} * {nombor2} = {nombor1 * nombor2}")
    elif operasi == 4:
        print(f"{nombor1} / {nombor2} = {nombor1 / nombor2}")

    bilangan_operasi += 1
    teruskan = input("\nMahu teruskan? (Y/T) : ").upper()

print('\n*****************************************')
print(f"Bilangan Operasi yang anda lakukan ialah: {bilangan_operasi}")
print("\nTERIMA KASIH..")
