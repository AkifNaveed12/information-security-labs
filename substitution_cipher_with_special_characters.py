# Extended Substitution Cipher (with special characters)

# Mehtod 1

key = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789 .,!?-"

def enc_substitution(n, plaintext):
    result = ''
    for l in plaintext:
        try:
            i = (key.index(l) + n) % len(key)
            result += key[i]
        except ValueError:
            result += l
    return result


def dec_substitution(n, ciphertext):
    result = ''
    for l in ciphertext:
        try:
            i = (key.index(l) - n) % len(key)
            result += key[i]
        except ValueError:
            result += l
    return result


origtext = "We hold these truths to be self-evident, that all men are created equal! 123"

ciphertext = enc_substitution(13, origtext)
plaintext = dec_substitution(13, ciphertext)

print("Original Text:", origtext)
print("Ciphertext:", ciphertext)
print("Decrypted Text:", plaintext)

#Method 2:
def enc_substitution(n, plaintext):
    result = ''
    for ch in plaintext:
        ascii_val = ord(ch)
        shifted = (ascii_val + n) % 128   # 128 = ASCII range
        result += chr(shifted)
    return result


def dec_substitution(n, ciphertext):
    result = ''
    for ch in ciphertext:
        ascii_val = ord(ch)
        shifted = (ascii_val - n) % 128
        result += chr(shifted)
    return result


origtext = "We hold these truths! 123"

ciphertext = enc_substitution(5, origtext)
plaintext = dec_substitution(5, ciphertext)

print("Original Text:", origtext)
print("Ciphertext:", ciphertext)
print("Decrypted Text:", plaintext)
