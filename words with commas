count_coma = 0
word_count = 0
words = []
with open('m5-line-by-line.txt', 'r') as fp:
    for line in fp:
        word_count += len(line.split())
        for word in line.split():
            if word[-1] == ',' or word[0] == ',':
                count_coma += 1
percent = int(count_coma / word_count * 100)
