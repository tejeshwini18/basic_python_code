"""Find the longest even-length word from a sentence."""

sentence = "Python programming is amazing for data analysis"
word_list = sentence.split()
len_dict = {}

for word in word_list:
    if len(word) % 2 == 0:
        len_dict[word] = len(word)

print(len_dict)
longest_word = max(len_dict, key=len_dict.get)
print(longest_word)
