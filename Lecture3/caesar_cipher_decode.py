class Decipher:
    text = "Khoor, Zruog!"  # "Hello, World!" shifted by +3
    shift_value = -3

    result = ""

    for ch in text:
        if ch.isupper():
            base = ord('A')
            offset = ord(ch) - base
            shifted = (offset + shift_value) % 26
            result += chr(base + shifted)

        elif ch.islower():
            base = ord('a')
            offset = ord(ch) - base
            shifted = (offset + shift_value) % 26
            result += chr(base + shifted)

        else:
            result += ch

    print("Encoded:", text)
    print("Decoded:", result)