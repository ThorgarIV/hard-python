puntuaction_marks = { ".", "!", "?" }
comma = ","
ending_keyword = "stop"

words_and_marks = []
text = ""
current_sentence = ""
sentences = []
total_words = 0
total_marks = 0
characters = {}
least_frequent_chars = []
most_frequent_chars = []
least_frequent_char_frequency = 1000000000
most_frequent_char_frequency = 0

print("\nType in one word at the time forming some sentences.")
print("Separate sentences with punctuation marks ( . ! ? ). You can use commas ( , ). To end type \"stop\"\n")

while text != ending_keyword:

    text = input("Add a word, type \"stop\" to end: ")

    words_and_marks.append(text)

# words_and_marks = ["ciao", ",", "mi", "chiamo", "Claudio", "!", "tu", "come", "ti", "chiami", "?", "ah", ",", "mi", "fa", "piacere"]

for index, text in enumerate(words_and_marks):

    for char in text:

        char = char.lower()

        if char in characters.keys():
            characters[char] += 1
        else:
            characters[char] = 1

    if text in puntuaction_marks:

        current_sentence += text

        sentences.append(current_sentence)

        current_sentence = ""

        total_marks += 1

    elif text == comma:

        current_sentence += text

        total_marks += 1

    else:

        if current_sentence == "":

            current_sentence += text.capitalize()

        else:
            
            current_sentence += " " + text
                
            if index == len(words_and_marks) - 1:
                sentences.append(current_sentence)
            
        total_words += 1

for index, sentence in enumerate(sentences):
    print(f"Sentence {index + 1}: \"{sentence}\"")

for frequency in characters.values():
    if frequency < least_frequent_char_frequency:
        least_frequent_char_frequency = frequency

    if frequency > most_frequent_char_frequency:
        most_frequent_char_frequency = frequency

for char, frequency in characters.items():
    if frequency == most_frequent_char_frequency:
        most_frequent_chars.append(char)

    if frequency == least_frequent_char_frequency:
        least_frequent_chars.append(char)

print(f"\nReceived {total_words} words.")
print(f"Received {total_marks} marks.")
print(f"Received {len(sentences)} sentences.")
print(f"Most frequent chars {most_frequent_chars} with a frequency of {most_frequent_char_frequency}")
print(f"Least frequent chars {least_frequent_chars} with a frequency of {least_frequent_char_frequency}")
        