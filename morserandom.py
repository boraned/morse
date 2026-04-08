from google import genai



client = genai.Client(api_key="YOUR API KEY")

import morse

def __main__():
    while 1:
        
        try:
            response = client.models.generate_content(
                model="gemini-2.5-flash",
                contents="Give me a single totally random word only and nothing else. This is for a random single word game. ALL CAPITAL LETTERS, NOT SO EASY TO GUESS WORD."
                
            )
            word = (response.text).upper()
        except Exception as e:
            print(f"Error found: {e}")
            return

        print("New word have been chosen.")

        while 1:
            morse.morse_play(word)
            if input("Enter result: ").upper() == word:
                print("Congrats! you found the word. Next one on the way.")
                break
            
            
                




__main__()