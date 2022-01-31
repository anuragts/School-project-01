def fn():
    f = open('test.txt', 'r')
    str = f.read()
    L = str.split()
    count_words = 0
    for i in L :
        count_words += 1
    print(f'Number of words : {count_words}')
    f.close()
if __name__ == '__main__':
    fn()