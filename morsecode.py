def encode_to_morse(text):
    """Converts text to Morse code."""
    morse_code = {
        'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.',
        'G': '--.', 'H': '....', 'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..',
        'M': '--', 'N': '-.', 'O': '---', 'P': '.--.', 'Q': '--.-', 'R': '.-.',
        'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-',
        'Y': '-.--', 'Z': '--..', '1': '.----', '2': '..---', '3': '...--',
        '4': '....-', '5': '.....', '6': '-....', '7': '--...', '8': '---..',
        '9': '----.', '0': '-----', ',': '--..--', '.': '.-.-.-', '?': '..--..',
        '/': '-..-.', '-': '-....-', ' ': '/', ';': '-.-.-.', ':': '---...',
        '\'': '.----.', '!': '-.-.--', '=': '-...-', '_': '..--.-',
        '(': '-.--.', ')': '-.--.-', '$': '...-..-', '@': '.--.-.'
    }
    return ' '.join(morse_code.get(char.upper(), '?') for char in text)


def decode_from_morse(morse):
    """Converts Morse code to text."""
    morse_to_alpha = {
        '.-': 'A', '-...': 'B', '-.-.': 'C', '-..': 'D', '.': 'E', '..-.': 'F',
        '--.': 'G', '....': 'H', '..': 'I', '.---': 'J', '-.-': 'K', '.-..': 'L',
        '--': 'M', '-.': 'N', '---': 'O', '.--.': 'P', '--.-': 'Q', '.-.': 'R',
        '...': 'S', '-': 'T', '..-': 'U', '...-': 'V', '.--': 'W', '-..-': 'X',
        '-.--': 'Y', '--..': 'Z', '.----': '1', '..---': '2', '...--': '3',
        '....-': '4', '.....': '5', '-....': '6', '--...': '7', '---..': '8',
        '----.': '9', '-----': '0', '--..--': ',', '.-.-.-': '.', '..--..': '?',
        '-..-.': '/', '-....-': '-', '/': ' ', '-.-.-.': ';', '---...': ':',
        '.----.': '\'', '-.-.--': '!', '-...-': '=', '..--.-': '_',
        '-.--.': '(', '-.--.-': ')', '...-..-': '$', '.--.-.': '@'
    }

    words = morse.split(" / ")  # Split Morse code words
    decoded_words = []

    for word in words:
        decoded_letters = [morse_to_alpha.get(code, '?') for code in word.split()]
        decoded_words.append("".join(decoded_letters))

    return " ".join(decoded_words)


# Main Execution
while True:
    print("\n1 - Encode to Morse Code")
    print("2 - Decode from Morse Code")
    print("3 - Exit")

    try:
        option = int(input("\nEnter your option: "))
        if option == 1:
            text = input("Enter text to encode: ")
            print("\nMorse Code:", encode_to_morse(text))
        elif option == 2:
            morse = input("Enter Morse code to decode: ")
            print("\nDecoded Text:", decode_from_morse(morse))
        elif option == 3:
            print("Exiting... Goodbye!")
            break
        else:
            print("Invalid option! Please enter 1, 2, or 3.")
    except ValueError:
        print("Invalid input! Please enter a number (1, 2, or 3).")
