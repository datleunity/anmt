alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ "

def rsa(mess):
    mess = mess.upper()
    p = 2
    q = 11
    n = p * q
    phi_n = (p-1) * (q-1)
    e = 7
    if e > 1 & e < phi_n :
        d = pow(e,-1,phi_n)
        print(f"public key (e,n) : ({e},{n})")
        print(f"private key (d,n) : ({d},{n})")
        
        encrypt = []
        for letter in mess:
            if letter in alpha:
                letter_index = alpha.find(letter) 
                ciphertext = pow (letter_index,e,n)
                encrypt.append(ciphertext)
         
            
        print(f"\nBan ro ban dau : {mess}")
        print(f"Ban ma hoa (c) : {encrypt}")
        
        res = ""
        for c in encrypt:
            decrypt_mes = pow(c,d,n)
            decrypt_mes = decrypt_mes % 26
            res += alpha[decrypt_mes]
        print(f"Ban sau giai ma : {res}")
        if (mess == res):
            print("=>Thanh cong! Giai ma trung khop voi tin nhan goc.")
        else:
            print("=>That bai !.")
                 
def main():
    word = "letandat"
    rsa(word)

main()