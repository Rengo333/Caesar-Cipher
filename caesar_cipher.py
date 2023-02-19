

def main():

    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    # main loop
    while True:

        choice = input("Do you want to (e)ncrypt or (d)ecrypt? ")
        # choice input check
        if choice != 'e' and choice != 'd':
            print("Please type either 'e' for encrypt or 'd' for decrypt")
            continue

        # key input check
        try:
            key = int(input("Please enter the key (0 to 25) to use. "))

            if key > 25 or key < 1 and key != 0:
                print("Key must be 0 to 25")
                continue

        except ValueError:
            print("Numbers only.")
            continue

        message = input("Enter the message to encrypt. ").upper()

        # if key is 0 message is returned in uppercase
        if key == 0:
            return print(message)

        # choice input check
        if choice == "e":
            return print(encrypt(message, key, alphabet))

        elif choice == "d":
            return print(decrypt(message, key, alphabet))


def encrypt(message, key, alphabet):

    encrypted = []

    for char in message:

        # check if it is a letter and find a position of a new letter
        if char.isalpha():
            char = alphabet.index(char) + key

            # check if position is in the alphabet
            if char > 26 or char == 26:
                char = char % 26
                encrypted.append(alphabet[char])

            else:
                encrypted.append(alphabet[char])

        # ignore character if its not a letter
        elif not char.isalpha():
            encrypted.append(char)

    # return list as a string
    return "".join(encrypted)


def decrypt(message, key, alphabet):

    decrypted = []

    for char in message:

        # check if it is a letter and find a position of a new letter
        if char.isalpha():
            char = alphabet.index(char) - key

            # check if position is in the alphabet
            if char < -26:
                char = char % - 26
                decrypted.append(alphabet[char])

            else:
                decrypted.append(alphabet[char])
        # ignore character if its not a letter
        elif not char.isalpha():
            decrypted.append(char)

    # return list as a string
    return "".join(decrypted)


if __name__ == "__main__":
    main()
