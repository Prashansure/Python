text = input("Enter a sentence: ")

# Count words
words = text.split()
word_count = len(words)

# Count vowels
vowels = "aeiouAEIOU"
vowel_count = 0
for char in text:
    if char in vowels:
        vowel_count += 1

# Count special characters
special_count = 0
for char in text:
    if not char.isalnum() and char != " ":
        special_count += 1

# Most frequent word
freq = {}
for word in words:
    freq[word] = freq.get(word, 0) + 1

most_frequent = max(freq, key=freq.get)

# Replace inappropriate words
bad_word = "bad"
text = text.replace(bad_word, "***")

# Output
print("Word Count:", word_count)
print("Vowel Count:", vowel_count)
print("Special Characters:", special_count)
print("Most Frequent Word:", most_frequent)
print("Updated Text:", text)