# week 6/CalHamlet.py

# 无法打开文件
# 要绝对路径
# the long url is broken into 3 parts by "r"......""
# the first "r" breaks the long url
# the second "r" is argument of the function open()

def getText():
    long_url = (r"/Volumes/MY-USB-2/Learning Python/My-Courses/"
                r"MOOC-Python-Foundation/week 6/"
                r"hamlet.txt"
    )
    txt = open(long_url, "r").read()
    txt = txt.lower()
    for ch in '!"#$%&()*+,-./:;<=>?@[\\]^_‘{|}~':
        txt = txt.replace(ch, " ")   #将文本中特殊字符替换为空格
    return txt
hamletTxt = getText()
words  = hamletTxt.split()
counts = {}
for word in words:			
    counts[word] = counts.get(word,0) + 1
items = list(counts.items())
items.sort(key=lambda x:x[1], reverse=True) 
for i in range(10):
    word, count = items[i]
    print ("{0:<10}{1:>5}".format(word, count))