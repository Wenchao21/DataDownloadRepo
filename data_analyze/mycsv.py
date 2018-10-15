import csv
import json
import jieba
import jieba.analyse
import redis

#import redis sql

pool = redis.ConnectionPool(host="127.0.0.1", port=6379)

r = redis.Redis(connection_pool=pool,db=2)

r.set('ttt', 'hewenchao')



decade = []
title = []
author_name = []
with open('result.csv') as f:
    reader = csv.reader(f)
    for wordsss in reader:
#        print(wordsss[0])
        decade.append(wordsss[0])
        title.append(wordsss[2])
        author_name.append(wordsss[3])


New_title = set(decade)
New_title.remove('author_decade')

list22 = list(New_title)
num = len(New_title)
print("All decae: %s, total: %s"%(list22,num))

countsong = 0

for i in range(0, len(New_title)-1):
    for j in range(0, len(decade)-1):
        if str(decade[j]) == str(list22[i]):
            countsong = countsong + 1
print(countsong)
#        seg_list = jieba.cut(str(wordsss[0]), cut_all=False)
#        print("/".join(seg_list))
#        string1 = string1 + str("/".join(seg_list))

#cipin fenxi

#tags = jieba.analyse.extract_tags(string1, topK=100)
#print(tags)
#print(','.join(seg_list))

#import jieba.posseg
#words = jieba.posseg.cut(string1)


#for w in words:
#    print(w.word)
#    print(w.flag)
