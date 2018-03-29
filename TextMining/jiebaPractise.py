# coding=utf-8
import jieba as jieb
import jieba.posseg
import jieba.analyse


sentence="我们是小学生来小学报到我们很高兴"


w1=jieb.cut(sentence,cut_all=False)  #cut_all=false 为精准的切分模式，默认为精准模式

for item in w1:
    print item

w2=jieb.cut_for_search(sentence) #按照搜索引擎的方式进行

for item in w2:
    print item

#词性标注
w3=jieb.posseg.cut(sentence)
for item in w3:
    print item.word+"---"+item.flag

#同样可以设置以及加载自己的词典，用来做词义分析

#提取文本中最常见的4个关键词
tag=jieb.analyse.extract_tags(sentence,4)

#print tag

#返回词语的位置
w5=jieb.tokenize(sentence)
for item in w5:
    print item



#文本相似度分析，可以根据相似度高的书籍进行读者推荐，也可以判断是哪类小说甚至说是否抄袭



