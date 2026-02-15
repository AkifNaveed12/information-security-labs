key = "abcdefghijklmnopqrstuvwxyz"

def enc_substitution(n, plaintext):
    result=""
    for  i in plaintext.lower():
        try:
            i = (key.index(i) + n) % 26
            result += key[i]
        except:
            result +=i
            
    return result

def dec_substitution(n, ciphertext):
    result=""
    for i in ciphertext.lower():
        try:
            i = (key.index(i) - n) % 26
            result += key[i]
            
        except:
            result += i
    return result


plaintext = "this is a test"
print("Plain text: ",plaintext)
ciphertext = enc_substitution(3, plaintext)
print("Plain to Cipher: ",ciphertext)
print("Cipher -> Plain : ",dec_substitution(3, ciphertext))

print("trying put some custom stuff.....")

Plaintext = input("\n\nEnter the text you want to encrypt: ")
print("custom plain text: ",Plaintext)

ciphertext = enc_substitution(13, Plaintext)
print("Plain to Cipher: ",ciphertext)
print("Cipher -> Plain : ",dec_substitution(13, ciphertext))