import random

print("WELCOME TO CODER AND DECODER ")


for _ in range(2) :
    try:
        a = int(input("Select 1 for coding and 2 for decoding: "))
        if a < 1 or a > 2:
            print("Please enter a valid value (1 or 2)")
            continue
        else:
            if a == 1:
                while True:
                    try:
                        yx = int(input("Please select 1 for binary conversion and 2 for reversal conversion: "))
                        if yx != 1 and yx != 2:
                            print("Please enter a valid value (1 or 2)")
                            continue
                        elif yx == 1:
                            # Binary conversion logic
                            text = input("Please enter the text you want to convert: ")
                            print("Converting to binary...")
                            binary = ''.join(format(ord(char), '08b') for char in text)
                            print(f"Your text has been converted to binary: {binary}")
                        elif yx == 2:
                            # Reversal conversion logic
                            text = input("Please enter the text you want to convert:- ")
                            print("converting the text...")
                            reversed_text = ''.join(reversed(text))
                            random_letters = ''.join(random.choices("jdnwrbifnkdcjvfsbiuiwtrbjsvnaiheinopv", k=2))
                            coded_text = reversed_text + random_letters
                            print(f"Your text has been coded: {coded_text}")
                        break
                    except ValueError:
                        print("Please enter a number (1 or 2) according to the options")
                        continue
            elif a == 2:

                while True:
                    try:
                        hx=int(input('Enter 1 for binary decodng and 2 for reversal decoding:- '))
                        if hx!=1 and hx!= 2:
                            print("please Enter a valid value (1 or 2)")
                            continue
                        elif hx==1:
                            text=input('please enter thr binary code you want to decode:- ')
                            text3=text.replace(' ' , '')
                            binary_chunks = [text3[i:i + 8] for i in range(0, len(text3), 8)]
                            original_text = ''.join(chr(int(chunk, 2)) for chunk in binary_chunks)



                            print(f'your decoded text is:-  {original_text }')


                        elif hx==2:
                            # Decoding logic
                            text = input("Please enter the text you want to decode: ")
                            print("Decoding...")
                            decoded_text = text[:-2][::-1]
                            print(f"Decoded text is: {decoded_text}")
                            break
                    except ValueError:
                        print('please enter a valid number ')
                        continue


    except ValueError:
                        print("Please enter a number (1 or 2) according to the options")
                        continue
    
