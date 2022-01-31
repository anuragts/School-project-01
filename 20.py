import collections

fin = open('input.txt', 'r')
a = fin.read()
d = {}
L =a.lower().split()

for word in L:
    word = word.replace(".", "")
    word = word.replace(",", "")
    word = word.replace(":", "")
    word = word.replace("\"","")
    word = word.replace("!", "")
    word = word.replace("&", "")
    word = word.replace("*","")

for k in L:
    key = k
    if key not in d:
        count = L.count(key)
        d[key] = count

n_print = int(input("How many most common words to print :"))

print("\n OK. The {} most common word are as follows \n".format(n_print))
word_counter = collections.Counter(d)
for word, count in word_counter.most_common(n_print):
    print(word, ":", count)
fin.close()