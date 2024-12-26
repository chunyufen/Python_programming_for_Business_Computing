# week 1/健康食谱输出.py

diet = ['西红柿', '花椰菜', '黄瓜', '牛排', '虾仁']
for x in range(0, 5):
    for y in range(0, 5):
        if not(x == y):
            print("{}{}".format(diet[x], diet[y]))