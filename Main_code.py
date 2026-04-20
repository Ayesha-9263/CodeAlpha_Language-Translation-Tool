from deep_translator import GoogleTranslator
print("===AI Translator===")

def run_translate():
    _input_text = input("Enter text: ")
    source = input("Enter source language (en, hi, fr): ")
    target = input("Enter target language: ")

    translated = GoogleTranslator(source=source, target=target).translate(_input_text)

    print("\nTranslated Text:")
    print(translated)

run_translate()
while True:
    run_translate()

    choice = input("Continue? (Yes/No): ")
    if choice.lower() != "yes":
        print("Program Ended.")
        break