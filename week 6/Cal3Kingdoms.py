# week 6/Cal3Kingdoms.py

# 无法打开文件
# 要绝对路径
# the long url is broken into 3 parts by "r"......""
# the first "r" breaks the long url
# the second "r" is argument of the function open()


import jieba
excludes = {}#{"将军","却说","丞相"}
long_url = (r"/Volumes/MY-USB-2/Learning Python/"
            r"My-Courses/MOOC-Python-Foundation/"
            r"week 6/threekingdoms.txt"
            )
txt = open(long_url, "r", encoding='utf-8').read()
words  = jieba.lcut(txt)
counts = {}
for word in words:
    if len(word) == 1:
        continue
    else:
        counts[word] = counts.get(word,0) + 1
for word in excludes:
    del(counts[word])
items = list(counts.items())
items.sort(key=lambda x:x[1], reverse=True) 
for i in range(15):
    word, count = items[i]
    print ("{0:<10}{1:>5}".format(word, count))