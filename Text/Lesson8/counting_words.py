def promptUserforFile():
    while True:
        fileName = input("Enter file:")
        # will input name below in terminal
        FileLocation = 'Text\\Lesson8'
        filePath = (f'{FileLocation}\\{fileName}')
        
        print(filePath)
        try:
            file = open(filePath)
            return file
        except:
            print('file not found')

file = promptUserforFile()
histogram = dict()
for line in file:
    for word in line.split():
        histogram[word] = histogram.get(word,0) + 1

biggestNumber = None
mostCommonWord = None

for word, count in histogram.items():
    if biggestNumber is None or count > biggestNumber:
        mostCommonWord = word
        biggestNumber = count

print(f'the most common word at {biggestNumber} is \'{mostCommonWord}\'')
# to print ', put \ infront of '