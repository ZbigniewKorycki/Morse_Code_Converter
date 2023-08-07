from morse_code import morse


def encrypt_to_morse(text_to_code):
    encrypted_characters = [morse[character] for character in text_to_code]
    encrypted_code = " ".join(encrypted_characters)
    return encrypted_code


def decrypt_morse(morse_code_to_decode):
    morse_code_separate_characters = morse_code_to_decode.split(" ")
    decrypted_code_separate_characters = []
    for single_character_code in morse_code_separate_characters:
        decrypted_character = [character for character, value in morse.items() if value == single_character_code][0]
        decrypted_code_separate_characters.append(decrypted_character)
    decrypted_code = "".join(decrypted_code_separate_characters)
    return decrypted_code


def morse_converter():
    converter_on = True
    while converter_on:
        encrypt_or_decrypt = input("Do you want to encrypt or decrypt morse code? Type (encrypt/decrypt): ").lower()
        if encrypt_or_decrypt == "encrypt":
            text_to_encrypt = input("What text do you want to encode into Morse code:\n").upper()
            code = encrypt_to_morse(text_to_encrypt)
            print(f"Morse code of your text '{text_to_encrypt}' is: {code}")
        elif encrypt_or_decrypt == "decrypt":
            text_to_decrypt = input("What Morse's code do you want to decrypt\n").upper()
            text = decrypt_morse(text_to_decrypt)
            print(f"Morse code of your Morse's code '{text_to_decrypt}' is: {text}")
        else:
            print("Incorrect input, type encrypt or decrypt.")
        reload = input("Do you want to encrypt/decrypt again? Type yes/no: ").lower()
        if reload == "yes":
            converter_on = True
        else:
            converter_on = False


morse_converter()
