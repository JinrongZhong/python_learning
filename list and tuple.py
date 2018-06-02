# -*- coding: utf-8 -*-
"""
Created on Sat Jun 02 15:56:53 2018

@author: ZJR

"""

'''
list 
有序集合
'''

list_example = ['one','three','four']

###可以采用索引访问，正序：0,1,2,3......；逆序：-1,-2,-3....,但是不要超出索引
#正序索引输出
for i in range(len(list_example)):
    print list_example[i]
#逆序索引输出
for i in range(-1,-len(list_example)-1,-1):
    print list_example[i]
    
###添加元素
#队尾追加
list_example.append('five')
print list_example

#指定位置插入
list_example.insert(1,'two')
print list_example

#删除队尾，可以用pop(),删除指定位置元素pop(i)
list_example.pop()
print list_example

list_example.pop(1)
print list_example

#删除第一次出现的某元素
L = ['one','two','three','four','five','two']
print L
L.remove('two')
print L
L.count('two')    #该元素在列表中出现的个数
L.index('two')    #该元素的位置,无则抛异常 
L.extend(list_example)  #追加list，即合并list到L上
L.sort()        #排序
L.reverse()     #倒序


##list里面的元素的数据类型也可以不同
l = ['Apple', 123, True]

##list元素也可以是另一个list
s = ['python', 'java', ['asp', 'php'], 'scheme']


##清空list
l = []



'''
有序列表:元组(tuple)
tuple 一旦定义就不可变
'''
t = (1,2)
t = ()#定义一个空的元组
t = (1,)#特别注意，定义只有一个元素的元组必须添加，

#可变元祖
t = ('a','b',['c','d'])
print t
t[2][0] = 'x'
t[2][1] = 'y'
print t

'''
说明，tuple 的元素仍旧是'a','b',list,
list元素变了，但是tuple指向的list没变
'''