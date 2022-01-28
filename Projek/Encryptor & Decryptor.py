from time import sleep
import string as s

semua_huruf = s.ascii_letters
huruf_besar = s.ascii_uppercase
huruf_kecil = s.ascii_lowercase


def pembahagi():
    print("------------------------------------------------------\n")


def text_result(encrypt_decrypt, teks_akhir):
    if encrypt_decrypt == 1:
        print("\n[Teks Sifer]: " + teks_akhir)
    elif encrypt_decrypt == 2:
        print("\n[Teks Biasa]: " + teks_akhir)


def songsang_abjad(teks_sementara):
    abc = semua_huruf + " "
    abc_songsang = huruf_kecil[::-1] + huruf_besar[::-1] + " "

    teks_songsang = ""
    for i in teks_sementara:
        nombor_huruf = abc.index(i)
        teks_songsang += abc_songsang[nombor_huruf]
    return teks_songsang


def songsang_perkataan(teks_sementara):
    teks_songsang = ' '.join(w[::-1] for w in teks_sementara.split())
    return teks_songsang


def songsang_mesej(teks_sementara):
    teks_songsang = teks_sementara[::-1]
    return teks_songsang


def reverse():
    pembahagi()
    print("==============")
    print("REVERSE CIPHER")
    print("==============\n")
    print("[ 1 ] Penyulitan")
    print("[ 2 ] Nyahsulit\n")
    encrypt_decrypt = int(
        input("> Pilih apa yang hendak anda lakukan (1,2): "))

    if encrypt_decrypt == 1:
        teks_sementara = input("\n> Taip teks yang hendak disulitkan: ")
    elif encrypt_decrypt == 2:
        teks_sementara = input("\n> Taip teks yang hendak dinyahsulit: ")

    print("\n>> JENIS REVERSE CIPHER <<")
    print("[ 1 ] Songsangan berdasarkan abjad (A-Z)")
    print("[ 2 ] Songsangan berdasarkan perkataan")
    print("[ 3 ] Songsangan berdasarkan seluruh mesej")

    pilihan_reverse = int(
        input("\n> Pilih jenis REVERSE CIPHER yang dikehendaki (1,2,3): "))

    if pilihan_reverse == 1:
        teks_songsang = songsang_abjad(teks_sementara)
    elif pilihan_reverse == 2:
        teks_songsang = songsang_perkataan(teks_sementara)
    elif pilihan_reverse == 3:
        teks_songsang = songsang_mesej(teks_sementara)

    text_result(encrypt_decrypt, teks_songsang)

    sleep(2)
    menu()


def caesar_cipher(teks_sementara, kunci, encrypt_decrypt):

    shifted_huruf_besar = huruf_besar[-kunci:] + huruf_besar[:-kunci]
    shifted_huruf_kecil = huruf_kecil[-kunci:] + huruf_kecil[:-kunci]

    teks_caesar = ""
    for huruf in teks_sementara:
        if encrypt_decrypt == 1:
            if huruf in huruf_besar:
                nombor_huruf = huruf_besar.index(huruf)
                teks_caesar += shifted_huruf_besar[nombor_huruf]
            elif huruf in huruf_kecil:
                nombor_huruf = huruf_kecil.index(huruf)
                teks_caesar += shifted_huruf_kecil[nombor_huruf]
            else:
                teks_caesar += huruf
        elif encrypt_decrypt == 2:
            if huruf in huruf_besar:
                nombor_huruf = shifted_huruf_besar.index(huruf)
                teks_caesar += huruf_besar[nombor_huruf]
            elif huruf in huruf_kecil:
                nombor_huruf = shifted_huruf_kecil.index(huruf)
                teks_caesar += huruf_kecil[nombor_huruf]
            else:
                teks_caesar += huruf

    return teks_caesar


def caesar():
    pembahagi()
    print("=============")
    print("CAESAR CIPHER")
    print("=============\n")

    print("[ 1 ] Penyulitan")
    print("[ 2 ] Nyahsulit\n")
    encrypt_decrypt = int(
        input("> Pilih apa yang hendak anda lakukan (1,2): "))

    if encrypt_decrypt == 1:
        teks_sementara = input("\n> Taip teks yang hendak disulitkan: ")
        kunci = int(input("> Kunci (1 - 25): "))
    elif encrypt_decrypt == 2:
        teks_sementara = input("\n> Taip teks yang hendak dinyahsulit: ")
        kunci = int(input("> Kunci (1 - 25): "))

    teks_caesar = caesar_cipher(teks_sementara, kunci, encrypt_decrypt)
    text_result(encrypt_decrypt, teks_caesar)

    sleep(2)
    menu()


def menu():
    pembahagi()
    print(">> JENIS-JENIS SIFER <<")
    print("[ 1 ] Reverse Cipher")
    print("[ 2 ] Caeser Cipher")

    pilihan_sifer = int(
        input("\n> Pilih jenis sifer yang dikehendaki (1,2): "))
    if pilihan_sifer == 1:
        reverse()
    elif pilihan_sifer == 2:
        caesar()


def kredit():
    pembahagi()
    print("======")
    print("KREDIT")
    print("======\n")
    print("Pencipta: Aidil Iskandar")
    print("Link Github: https://github.com/aidil-sekandar/Projek-Python/blob/main/Projek/Encryptor%20&%20Decryptor.py")
    print("\n=============")
    print("Terima Kasih!")
    print("=============\n")

    sleep(3)
    pembahagi()
    main()


def main():
    print("======================")
    print("ENCRYPTOR & DECRYPTOR!")
    print("======================\n")
    print(">> Menu <<")
    print("[ 1 ] Mula")
    print("[ 2 ] Kredit")
    print("[ 3 ] Keluar")

    pilihan = int(input("\n> Pilih satu menu (1,2,3): "))
    if pilihan == 1:
        menu()
    elif pilihan == 2:
        kredit()
    elif pilihan == 3:
        print("\nTerima kasih!")
        pembahagi()
        sleep(2)
        exit()

if __name__ == "__main__":
    main()
