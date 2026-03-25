"""Create a dictionary from words to their lengths."""

text = "I like to learn new things"
lengths = {}
for word in text.split():
    lengths[word] = len(word)

print(lengths)
