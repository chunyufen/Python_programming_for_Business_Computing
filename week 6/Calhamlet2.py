# week 6/Calhamlet2.py

# 无法打开文件
# 要绝对路径
# the long url is broken into 3 parts by "r"......""
# the first "r" breaks the long url
# the second "r" is argument of the function open()

excludes = {"the","and","of","you","a","i","my","in"}
def getText():
    long_url = (r"/Volumes/MY-USB-2/Learning Python/"
               r"My-Courses/MOOC-Python-Foundation/"
               r"week 6/hamlet.txt"
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
for word in excludes:
    del(counts[word])    
items = list(counts.items())
items.sort(key=lambda x:x[1], reverse=True) 
for i in range(10):
    word, count = items[i]
    print ("{0:<10}{1:>5}".format(word, count))