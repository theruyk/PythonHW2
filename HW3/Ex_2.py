# В большой текстовой строке text подсчитать количество встречаемых слов и вернуть
#  10 самых частых. Не учитывать знаки препинания и регистр символов.
import string
from collections import Counter

def remove_punctuation(sentence):
    sentence = sentence.replace("'", " ").replace("-", " ")
    return ''.join(char for char in sentence if char not in string.punctuation)

def count_words(text):
  words = text.lower().split()
  return Counter(words)

def remove_digits(input_string):
    translation_table = str.maketrans('', '', '0123456789')
    result = input_string.translate(translation_table)
    return result


# text = 'Hello world. Hello Python. Hello again.'
# text = "Python 3.9 is the latest version of Python. It's awesome!"
text = "Python is an interpreted, high-level, general-purpose programming language. Created by Guido van Rossum and first released in 1991, Python's design philosophy emphasizes code readability with its notable use of significant whitespace. Its language constructs and object-oriented approach aim to help programmers write clear, logical code for small and large-scale projects."


reducted_text = remove_punctuation(text)
no_digits = remove_digits(reducted_text)
word_counts = count_words(no_digits)
most_common_words = word_counts.most_common(10)
print(most_common_words)

