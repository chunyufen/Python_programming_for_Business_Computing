# week 6/Cal3Kingdoms2.py

# 无法打开文件
# 要绝对路径
# the long url is broken into 3 parts by "r"......""
# the first "r" breaks the long url
# the second "r" is argument of the function open()


import jieba
excludes = {"将军","却说","荆州","二人","不可","不能","如此"}
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
    elif word == "诸葛亮" or word == "孔明曰":
        rword = "孔明"
    elif word == "关公" or word == "云长":
        rword = "关羽"
    elif word == "玄德" or word == "玄德曰":
        rword = "刘备"
    elif word == "孟德" or word == "丞相":
        rword = "曹操"
    else:
        rword = word
    counts[rword] = counts.get(rword,0) + 1
for word in excludes:
    del(counts[word])
items = list(counts.items())
items.sort(key=lambda x:x[1], reverse=True) 
for i in range(5):
    word, count = items[i]
    print ("{0:<10}{1:>5}".format(word, count))