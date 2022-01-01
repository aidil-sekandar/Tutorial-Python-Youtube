print("""==================
Sila pilih operasi
==================
1. +
2. -
3. ×
4. ÷""")

teruskan = "Y"
while teruskan == "Y":

    operasi = int(input("\nSila pilih operasi (1/2/3/4) : "))
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

    teruskan = input("\nMahu teruskan? (Y/T) : ").upper()

print("\n=============")
print("Terima Kasih!")
print("=============")
