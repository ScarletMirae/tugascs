def caesar_cipher(text, shift):
    result = ""
    for char in text:
        if char.isalpha():
            shift_base = 65 if char.isupper() else 97
            result += chr((ord(char) - shift_base + shift) % 26 + shift_base)
        else:
            result += char
    return result


def vigenere_cipher(text, key):
    result = []
    key = key.lower()
    key_index = 0

    for char in text:
        if char.isalpha():
            shift = ord(key[key_index]) - ord('a')
            shift_base = 65 if char.isupper() else 97
            result.append(chr((ord(char) - shift_base + shift) % 26 + shift_base))
            key_index = (key_index + 1) % len(key)
        else:
            result.append(char)

    return ''.join(result)


def transposition_cipher(text, key):
    columns = [''] * key
    for col in range(key):
        pointer = col
        while pointer < len(text):
            columns[col] += text[pointer]
            pointer += key
    return ''.join(columns)


def main():
    print("Pilih algoritma kriptografi klasik:")
    print("1. Caesar Cipher")
    print("2. Vigenère Cipher")
    print("3. Transposisi Cipher")

    choice = input("Masukkan pilihan (1/2/3): ")

    if choice == '1':
        text = input("Masukkan teks yang akan dienkripsi: ")
        shift = int(input("Masukkan nilai shift: "))
        encrypted = caesar_cipher(text, shift)
        print("Hasil enkripsi Caesar Cipher:", encrypted)

    elif choice == '2':
        text = input("Masukkan teks yang akan dienkripsi: ")
        key = input("Masukkan kunci: ")
        encrypted = vigenere_cipher(text, key)
        print("Hasil enkripsi Vigenère Cipher:", encrypted)

    elif choice == '3':
        text = input("Masukkan teks yang akan dienkripsi: ")
        key = int(input("Masukkan kunci (integer): "))
        encrypted = transposition_cipher(text, key)
        print("Hasil enkripsi Transposisi Cipher:", encrypted)

    else:
        print("Pilihan tidak valid.")


if __name__ == "__main__":
    main()