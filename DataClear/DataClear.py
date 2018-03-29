# coding=utf-8
import pandas as pda
import numpy  as npy


#数据集成结果
a=npy.array([[2,3,4,5],[6,5,3,2]])
b=npy.array([[4,2,7,4],[8,3,1,0]])

c=npy.concatenate((a,b))


d=npy.array([2,4,6,7,8,9])

print pda.cut(d,[3,5,7,9],labels=["第一号","第二号","第三号"]) # 对数据进行离散化处理


#data.to_excel(路径，index=)  可以将数据写入到文件中
