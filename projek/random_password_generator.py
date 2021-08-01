import random 
import string

print("Welcome to Password Generator")
print("=============================")

chars = string.ascii_letters + string.digits + string.punctuation

amount = int(input('Pasword amount? : '))
length = int(input('Pasword length? : '))
print("\nhere are your password: ")

for i in range(amount):
    passwords = ""
    for j in range(length):
        passwords += random.choice(chars)
    print(passwords)
