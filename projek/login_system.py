account_data = {
    "aidil" : "123",
    "iskandar" : "456"
}

print("---- Login to your account ----")
input_username = input("Enter your username: ")
if input_username not in account_data:
    print("Wrong Username!")
else:
    input_password = input("Enter your password: ")
    if input_password == account_data[input_username]:
        print("Login successful!")
    else:
        print("Wrong Password")
