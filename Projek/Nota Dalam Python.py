fail = open("nota.txt", "w+")
fail.write("NOTA ANDA:\n===========\n\n")
fail.close()
file = open("nota.txt", "a")


def menu():
    print("==================")
    print("Tuliskan nota anda")
    print("==================\n")
    print("Taip 'exit()' untuk berhenti menulis nota")
    print("Had adalah 20\n")
    main()


def main():
    for i in range(1, 21):
        nota = input(f"{i}. ")
        if nota == "exit()":
            break
        else:
            file.write(f"{nota}\n")

    print("\nTerima Kasih")
    file.close()


if __name__ == "__main__":
    menu()
