sentence = input("Enter a sentence: ")

# Split the sentence into words
words = sentence.split()

# Create an empty dictionary to store word counts
frequency = {}

# Count how many times each word appears
for word in words:
    if word in frequency:
        frequency[word] += 1   # increase count if word already exists
    else:
        frequency[word] = 1    # add new word with count 1

# Print the result
print("\nWord Frequency:")
for word, count in frequency.items():
    print(word, ":", count)