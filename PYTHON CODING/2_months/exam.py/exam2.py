m = "What are, called even number, are are"

# 1) Remove punctuation (, .) and convert to lowercase
n = m.lower()

for ch in [".", ","]:
    n = n.replace(ch, "")

print("Original:", m)
print("After removing punctuation:", n)

# 2) Split into words
words = n.split()

# 3) Stop words are only ',' and '.' 
stopword = [",", "."]
neww = []

for w in words:
    if w not in stopword:
        neww.append(w)

# 4) Compute word frequency (without external function)
freq = {}
for w in neww:
    if w in freq:
        freq[w] += 1
    else:
        freq[w] = 1

# 5) Display top 3 frequent words (manual sorting)
freq_list = list(freq.items())

for i in range(len(freq_list)):
    for j in range(i + 1, len(freq_list)):
        if freq_list[j][1] > freq_list[i][1]:
            freq_list[i], freq_list[j] = freq_list[j], freq_list[i]

top3 = freq_list[:3]

print("Words:", words)
print("Filtered words:", neww)
print("Frequencies:", freq)
print("Top 3 frequent words:", top3)
