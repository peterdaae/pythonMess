class Cipher:
    text = "Hello, World!"
    shift_value = 3

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
            # leave non-letters unchanged
            result += ch

    print("Original:", text)
    print("Encoded :", result)


