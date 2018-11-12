### 
### Author: Faye Bandet
### Course: CSC 110
### Description: This is a program that decrypts a file from the encrypter program.
###
def main():
    encrypted_text = input('Enter the name of a mixed text file: \n')
    index_file = input('Enter the mix index file: \n')
    open_i = open(index_file, 'r')
    open_f = open(encrypted_text, 'r')
    encrypt_l = open_f.readlines() ### Encrypt List
    index_l = open_i.readlines()   ### Index List
    decrypt_l = []                 ### Decrypt List
    decrypt_f = open('decrypted.txt', 'w')
    for i in range(len(index_l)):
        decrypt_l.append('')
    for i in range(len(decrypt_l)):
        decrypt_l[int(index_l[i]) - 1] = encrypt_l[i]
    for line in decrypt_l:
        decrypt_f.write(line)
    open_i.close()
    open_f.close()
    decrypt_f.close()
main()