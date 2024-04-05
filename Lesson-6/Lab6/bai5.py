
input_string = input("Enter a sentence: ")

unique_words = []

for word in input_string.split():
    if word not in unique_words:
        unique_words.append(word)

print("The number of unique words: " + str(len(unique_words)))