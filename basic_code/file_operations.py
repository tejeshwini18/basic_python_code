with open('sample.txt','r') as f:
	content = f.read()
print('content',content)

count_dict = {}
for word in content:
	if word in count_dict:
		count_dict[word] +=1
	else:
		count_dict[word] = 1
print(count_dict)
sorted_dict = {key:count_dict[key] for key in sorted(count_dict)}
# sorted_dict = sorted(count_dict.items(),key=lambda x:x[1],reverse=True)
print(sorted_dict)

top_5_words = sorted(count_dict.items(),key=lambda x:x[1],reverse=True)[:5]
for word,freq in top_5_words:
	print(word,freq)
	