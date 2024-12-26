# week 6/Calhamlet3.py

# 无法打开文件
# 要绝对路径
# the long url is broken into 3 parts by "r"......""
# the first "r" breaks the long url
# the second "r" is argument of the function open()

def getText():
    long_url = (r"/Volumes/MY-USB-2/Learning Python/"
               r"My-Courses/MOOC-Python-Foundation/"
               r"week 6/hamlet.txt"
               )
    with open(long_url, 'r') as f:
        text = f.read()
    return text

def getPunctuation(text):
    punc = set()
    for ch in text:
        if ord(ch) < ord('a')or ord(ch) > ord('z'):
            punc.add(ch)
    return punc

def getWords(text):
    text = text.lower()
    punc = getPunctuation(text)
    for p in punc:
        text = text.replace(p, ' ')
    return text.split(' ')

def countWord(words):
    counts = {}
    for word in words:
        if word == '':
            continue
        counts[word] = counts.get(word, 0) + 1
    return counts

words = getWords(getText())
counts = countWord(words)

items = list(counts.items())
items.sort(key=lambda x:x[1], reverse=True)
for i in range(10):
    word, count = items[i]
    print("{:<6}:{:>5}".format(word, count))
    