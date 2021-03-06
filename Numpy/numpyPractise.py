# coding=utf-8

import numpy
import pandas as pda
import pymysql
#添加注释的时候，需要在前边加上# coding=utf-8，不然会报编码错误
#定义数组的时候，括号里边要加上[]，不管是二维还是一维

array1=numpy.array(["2","9","8","a"])

array2=numpy.array([[3,13,10],[4,2,7],[8,3,6]])

#array1.sort()

#array2.sort()

print array2

#数组的切片选择元素

print  array1[1:3] #由此看出 数组下标是从0开始的

print array2[0]

print  array1



'''series index 索引  data.frame'''

a=pda.Series([8,9,3,4])
b=pda.Series([8,9,3,4],index=["one","two","three","four"])

#通过二维数组创建dataframe
c=pda.DataFrame([[1,2,3],[4,5,6],[7,8,9],[10,11,12]],columns=["one","two","three"])  #元素为二维数组的形式，每个元素代表一行，下标是从0开始

print c

#通过字典的方式创建dataframe,这样就直接设置了列名

d=pda.DataFrame({
    "one":4,
    "two":[6,2,3],
    "three":list( str(982))
})

print d
print list(str(982)) #list类型里的元素必须是str类型，需要进行强制转换
print d.head(2) #取默认前几行
print d.tail(2) #取后2行

#相当于R中的summary
print d.describe()

#读csv文件
#i=pda.read_csv()
#i.sort_values(by="") #按照个某列的值进行排序

#读excel文件
#h=pda.read_excel() #读取excel文件

#读取mysql数据库文件,在论文中用到是mysqldb
conn=pymysql.connect(host="127.0.0.1",user="root",password="123",db="dataSource")
sql="select account_id from matchPlayers;"
k=pda.read_sql(sql,conn)

#通过data.value[] 列数可以查出某一列里边的内容  

print k

#读取html网站中的表格数据

m=pda.read_html("http://mba.buaa.edu.cn/info/1072/3463.htm")

print m






