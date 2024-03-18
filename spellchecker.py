import re
from textblob import TextBlob

def read_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        return file.read()

def tokenize_text(text):
    return re.findall(r'\b\w+\b', text.lower())

def correct_spelling(word):
    blob = TextBlob(word)
    return str(blob.correct())

def main():
    file_path = input("Enter the path to the text file: ")
    text = read_file(file_path)

    words = tokenize_text(text)
    corrected_text = text

    for word in words:
        if len(word) > 1 and word.isalpha():
            corrected_word = correct_spelling(word)
            if corrected_word != word:
                corrected_text = re.sub(r'\b' + word + r'\b', f'{word} ({corrected_word})', corrected_text, flags=re.IGNORECASE)

    with open("corrected_text.txt", 'w', encoding='utf-8') as output_file:
        output_file.write(corrected_text)

    print("Spell check and correction completed. Corrected text saved to 'corrected_text.txt'.")

if __name__ == "__main__":
    main()
