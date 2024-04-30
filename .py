# scc.py

import sys

# function iterates over input text and shifts letters by requested number of shifts
def cipher(text, shift): 
    encrypted_text = " "
    for char in text:
        if char.isalpha():
            if char.isupper():
                offset = ord("A")
            else:
                offset = ord("a")
            encrypted_char = chr((ord(char) - offset + shift) % 26 + offset)
        else:
            encrypted_char = char
        encrypted_text += encrypted_char
    return encrypted_text

# function accepts user input
def blocks(text):
    for i in range(0, len(text), 5):
        print(text[i:i+5], end = " ")
    print()

def main():
    print("Enter a message to encrypt:")
    text = sys.stdin.readline().rstrip()
    shift = int(input("Enter number of shifts:  "))
    text = cipher(text, shift)
    print("Encrypted text:")
    blocks(text)

if __name__ == "__main__":
    main()
