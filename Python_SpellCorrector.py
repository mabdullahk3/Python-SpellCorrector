import nltk
from nltk.tokenize import word_tokenize, sent_tokenize
from nltk.corpus import wordnet
from nltk.stem import WordNetLemmatizer
from textblob import TextBlob
import re

nltk.download('punkt')
nltk.download('wordnet')

def extract_data(essay):
    # extracting words and determining word count
    words = re.findall(r'\b\w+\b', essay)
    word_count = len(words)
    # extracting sentences and determining sentence count
    sentences = essay.split('.')
    # remove empty strings
    sentences = [sentence.strip() for sentence in sentences if sentence.strip()]
    sentence_count = len(sentences)
    # unique words
    unique_words = set(words)
    unique_word_count = len(unique_words)
    return sentence_count, unique_word_count, word_count

def spell_check(essay):
    blob = TextBlob(essay)
    corrected_essay = str(blob.correct())
    mistakes = []
    for original, corrected in zip(blob.words, blob.correct()):
        if original != corrected:
            if '.' in original and '.' not in corrected:
                mistakes.append((original, original))
            else:
                mistakes.append((original, corrected))
    return corrected_essay, mistakes


def analyze_essay(essay):
    sentence_count, unique_word_count, word_count = extract_data(essay)
    corrected_essay, mistakes = spell_check(essay)

    print("Original sentence/essay: ")
    print(essay)
    print("\nSentence/essay analysis:" )
    print("Number of words: ", word_count)
    print("Number of sentences: ", sentence_count)
    print("Number of unique words: ", unique_word_count)

    print("\nCorrected sentence/essay: ")
    print(corrected_essay)

def main():
    essay = input("Enter the sentence/essay: ")
    analyze_essay(essay)

if __name__ == "__main__":
    main()

    