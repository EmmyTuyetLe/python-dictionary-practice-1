"""Count words in file."""
import sys
text_file = open(sys.argv[1]).read().replace("?", "").replace(".", "").replace("!", "").replace(",", "").replace(":", "").lower()
# def count_words(text):
#     counted_words = {}
#     text_list = text.split() #return list with each item as a separate index
#     for word in text_list:
#         counted_words[word] = counted_words.get(word, 0) +1
#     return counted_words
# # put your code here.
# result = count_words(text_file)
# print(result) 

def tokenize(text):
    text_list = text.split() #return list with each item as a separate index
    return text_list

def count_words(text_list):
    counted_words = {}
    for word in text_list:
        counted_words[word] = counted_words.get(word, 0) +1
    return counted_words

def print_word_counts(dictionary):
    print(dictionary.items())
    
