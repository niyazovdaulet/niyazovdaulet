alphabet = ['a', 'b', 'c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))


def encrypt(original_text, shift_amount):
    cipher_text = ""

    for letter in original_text:
        shiftted_position  = alphabet.index(letter) + shift_amount


        shiftted_position %= len(alphabet)
        cipher_text += alphabet[shiftted_position]

        print(f"Here is your encoded result: {cipher_text}")





encrypt(original_text=text, shift_amount=shift)
