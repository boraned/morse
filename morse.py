from playsound import playsound
import time



def morse_play(str): 
        
    morse = {
        'A': '.-',     'B': '-...',   'C': '-.-.',   'D': '-..',    'E': '.',
        'F': '..-.',   'G': '--.',    'H': '....',   'I': '..',     'J': '.---',
        'K': '-.-',    'L': '.-..',   'M': '--',     'N': '-.',     'O': '---',
        'P': '.--.',   'Q': '--.-',   'R': '.-.',    'S': '...',    'T': '-',
        'U': '..-',    'V': '...-',   'W': '.--',    'X': '-..-',   'Y': '-.--',
        'Z': '--..',   '1': '.----',  '2': '..---',  '3': '...--',  '4': '....-',
        '5': '.....',  '6': '-....',  '7': '--...',  '8': '---..',  '9': '----.',
        '0': '-----',  ', ': '--..--', '.': '.-.-.-', '?': '..--..', '/': '-..-.',
        '-': '-....-', '(': '-.--.',  ')': '-.--.-'
    }

    def morse_play_helper(char):
        #Play the "." or "-" sound
        if char =='.':
            playsound("dit.wav")
        elif char == "-":
            playsound("dah.wav")
        time.sleep(0.05)


    #Iterate over the string
    for i in range(len(str)):
        #Play the word
        for i in morse[str[i]]:
            morse_play_helper(i)
        
        time.sleep(0.3)