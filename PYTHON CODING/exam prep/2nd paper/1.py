comments = input().split(",")

unique_words = set()

for sentence in comments:
    words = sentence.strip().split()
    for word in words:
        unique_words.add(word)

print(unique_words)