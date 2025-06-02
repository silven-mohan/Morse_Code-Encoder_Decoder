morse_code_dict = {
    'A': '.-', 'B': '-...', 'C': '-.-.',
    'D': '-..', 'E': '.', 'F': '..-.',
    'G': '--.', 'H': '....', 'I': '..',
    'J': '.---', 'K': '-.-', 'L': '.-..',
    'M': '--', 'N': '-.', 'O': '---',
    'P': '.--.', 'Q': '--.-', 'R': '.-.',
    'S': '...', 'T': '-', 'U': '..-',
    'V': '...-', 'W': '.--', 'X': '-..-',
    'Y': '-.--', 'Z': '--..',
    '0': '-----', '1': '.----', '2': '..---',
    '3': '...--', '4': '....-', '5': '.....',
    '6': '-....', '7': '--...', '8': '---..',
    '9': '----.','a':'.-', 'b': '-...', 'c': '-.-.', 'd': '-..', 'e': '.', 'f': '..-.',
    'g': '--.', 'h': '....', 'i': '..', 'j': '.---', 'k': '-.-', 'l': '.-..',
    'm': '--', 'n': '-.', 'o': '---', 'p': '.--.', 'q': '--.-', 'r': '.-.',
    's': '...', 't': '-', 'u': '..-', 'v': '...-', 'w': '.--', 'x': '-..-',
    'y': '-.--', 'z': '--..','.': '.-.-.-', ',': '--..--', '?': '..--..', "'": '.----.',
    '!': '-.-.--', '/': '-..-.', '(': '-.--.', ')': '-.--.-',
    '&': '.-...', ':': '---...', ';': '-.-.-.', '=': '-...-',
    '+': '.-.-.', '-': '-....-', '_': '..--.-', '"': '.-..-.',
    '$': '...-..-', '@': '.--.-.',' ': ' '
    }
reverse_morse_code_dict = {v:k for k,v in morse_code_dict.items()}

mode=input("Type 'encode' to convert text to morse or 'decode' to convert morse to text")

if mode=='encode':
    text_input=input("Enter Text:")
    morse_output=""
    for char in text_input:
        if char in text_input:
            morse_output += morse_code_dict[char]
        elif char==" ":
            morse_output += " "
        else:
            morse_output += "?"
    print("Morse Code:",morse_output)
elif mode == 'decode':
    morse_input = input("Enter Morse Code: ")
    text_output = ""
    morse_code=morse_input.strip().split('/')
    for morse_code in morse_input:
        if morse_code in morse_input:
            text_output += reverse_morse_code_dict[morse_code]
    print("Decoded Morse Code:",text_output)
