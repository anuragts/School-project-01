import collections as co

def fn():
    fin = open('input.txt', 'r')
    a = fin.read()
    d = {}
    L =a.lower().split()
    lst = [",", ".", "!", "&",  ":", "\"", "*", ]

    for word in L:
        if word in lst:
            word = word.replace(word, "")

    for k in L:
        key = k
        if key not in d:
            count = L.count(key)
            d[key] = count

    n_print = int(input("How many most common words to print :"))

    print("\n OK. The {} most common word are as follows \n".format(n_print))
    word_counter = co.Counter(d)
    for word, count in word_counter.most_common(n_print):
        print(word, ":", count)
    fin.close()
fn()