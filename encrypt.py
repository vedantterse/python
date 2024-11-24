# Data Encryption -- using the ceaser cipher method
"""
FIle:  encrypt.py
Encrypt an input string of lowercase letters and prints the result. the other input is the disance value.
"""

plainText = input("Enter a one-word, lowercase message: ")
distance = int(input("Enter the distance value: "))
code = ""

for char in plainText:
    ordValue = ord(char)
    cipherValue = ordValue + distance
    if cipherValue > ord('z'):
        cipherValue = ord('a') + distance - (ord('z') - ordValue + 1)
    code += chr(cipherValue)
print(code)