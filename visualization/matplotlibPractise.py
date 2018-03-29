# coding=utf-8
import matplotlib.pylab as pyl
import numpy as npy

#折线图/散点图  plot
x=[1,2,3,4,5]
y=[5,6,5,3,9]


pyl.plot(x,y,'-.r') #设置线条的格式
#plot(x,y,展现形式)
pyl.plot(x,y,'or')  #o代表形状，r代表是红色,参数可以叠加

#pyl.title("test")
#pyl.xlabel("x")
#pyl.ylabel("y")
#pyl.xlim(0,5)
#pyl.xlim(0,10)
#pyl.show()

#第三个参数可以设置为  点的样式、线的样式、以及点线的颜色

r1=npy.random.random_integers(1,20,10)
r2=npy.random.random_integers(1,20,10)

r3=npy.random.normal(10.0,2.0,50)
pyl.hist(r3)
pyl.show()


#同样的可以设置轮廓是否保存，颜色、边框、横竖轴范围等

