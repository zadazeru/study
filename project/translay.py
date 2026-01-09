import translators as ts

def main():
    try:
        text_to_write= input("Enter the text you want to translate:")
        write_lang = input("Enter the language you want to translate ")
        translated_text = ts.translate_text(
            query_text=text_to_write,
            translator='google',
            from_language='auto',
            to_language=write_lang
        )
        print(f"Translated text: {translated_text}")
        print(f"Translated ({text_to_write}): {translated_text}")
    except Exception as e:
        print(f"An error occurred: {e}")
        
if __name__ == "__main__":
    main()