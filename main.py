# Dictionary representing the morse code chart
MORSE_CODE_DICT = {'A': '.-', 'B': '-...',
                   'C': '-.-.', 'D': '-..', 'E': '.',
                   'F': '..-.', 'G': '--.', 'H': '....',
                   'I': '..', 'J': '.---', 'K': '-.-',
                   'L': '.-..', 'M': '--', 'N': '-.',
                   'O': '---', 'P': '.--.', 'Q': '--.-',
                   'R': '.-.', 'S': '...', 'T': '-',
                   'U': '..-', 'V': '...-', 'W': '.--',
                   'X': '-..-', 'Y': '-.--', 'Z': '--..',
                   '1': '.----', '2': '..---', '3': '...--',
                   '4': '....-', '5': '.....', '6': '-....',
                   '7': '--...', '8': '---..', '9': '----.',
                   '0': '-----', ', ': '--..--', '.': '.-.-.-',
                   '?': '..--..', '/': '-..-.', '-': '-....-',
                   '(': '-.--.', ')': '-.--.-',
                   ' ': '/'}
CONTINUE = True

print("TEXT TO MORSE CODE CONVERTER")


# Function to convert text to Morse code
def text_to_morse(text):
    morse_result = []
    for letter in text.upper():
        if letter in MORSE_CODE_DICT:
            morse_result.append(MORSE_CODE_DICT[letter])
        else:
            morse_result.append('?')  # To handle unknown characters
    return ' '.join(morse_result)


# Function to interact with the user
def converter():
    continue_conversion = True
    while continue_conversion:
        user_text = input("Enter the text to convert to Morse code: ")
        morse_text = text_to_morse(user_text)
        print(f"Morse code translation for your text is: {morse_text}")
        response = input("Do you want to continue? (Y for yes, N for no): ")
        if response.strip().lower() not in ['y', 'yes']:
            continue_conversion = False

if __name__ == "__main__":
    converter()


