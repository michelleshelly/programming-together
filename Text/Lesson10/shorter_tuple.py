file = open('Text\Lesson8\words.txt')

word_histogram = dict()
result = 'the quick brown, fox,'.split()
print(result)

for line in file:
    line = line.replace('.', '')
    line = line.replace(',', '')
    words_in_line = line.split()
    for word in words_in_line:
        word_histogram[word] = word_histogram.get(word,0) + 1

# change here
value_key_list = sorted(
    [ (value,key) for key,value in word_histogram.items()],
    reverse=True
    )
#VS for key,value in word_histogram.items():
   # new_tuple = (value,key)
    #value_key_list.append(new_tuple)

# value_key_list = sorted(value_key_list, reverse=True)

for value, key in (value_key_list[:10]):
# takes 0th to 10th item
    print(key,value)