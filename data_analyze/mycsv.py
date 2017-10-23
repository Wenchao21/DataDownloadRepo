import csv
import json
import jieba
import jieba.analyse
with open('result.csv') as f:
    reader = csv.reader(f)
    string1 = ""
    for wordsss in reader:
        seg_list = jieba.cut(str(wordsss[1]), cut_all=False)
        print("/".join(seg_list))
        string1 = string1 + str("/".join(seg_list))

#cipin fenxi

tags = jieba.analyse.extract_tags(string1, topK=100)
print(tags)
print(','.join(seg_list))

#import jieba.posseg
#words = jieba.posseg.cut(string1)


#for w in words:
#    print(w.word)
#    print(w.flag)
