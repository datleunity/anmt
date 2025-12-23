
alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

def encrypt(key , mess):
    mess = mess.upper()
    res = ""
    for letter in mess:
        if letter in alpha: 
            letter_index = (alpha.find(letter) + key) % len(alpha)
            res = res + alpha[letter_index]
        else:
            res = res + letter
    return res
        
def decrypt (key,mess):
    mess = mess.upper()
    res = ""
    for letter in mess:
        if letter in alpha:
            letter_index = (alpha.find(letter) - key) % len(alpha)
            res = res +  alpha[letter_index]
        else:
            res = res + letter
    return res
    
def hacking(mess):
    mess = mess.upper()
    for key in range(len(alpha)):
        translated = decrypt(key,mess)
        print('Hacking key #%s: %s' % (key, translated))
    
        
        


def main():
    mess = "hello world"
    k = 3
    encrypted = encrypt(k,mess)
    decrypted = decrypt(k,encrypted)
    print("\nmess : "+mess)
    print("\nencrypted : "+encrypted)
    print("\ndecrypted : "+decrypted)
    
    hacking(encrypted)
    
main()
