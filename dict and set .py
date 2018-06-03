# -*- coding: utf-8 -*-
"""
Created on Sat Jun 02 16:39:30 2018

@author: ZJR


dict and set
"""

'''
python 中的dict在别的语言中也叫map，采用key-value 对的形式进行存储
1.dict内部存放的顺序和key放入的顺序是没有关系的
2.dict是用空间来换取时间的一种方法
3.dict的key必须是不可变对象 
'''

d = {'amy':90, 'jack':80, 'jack':80,'Michael':50, 'Sarah':80, 'Tracy':30, 'Bob':80}
d['amy'] = 67#赋值
d['amy'] #取值

##判断key是否存在
#一是通过in判断key是否存在
'amy' in d

#二是通过dict提供的get方法，如果key不存在，可以返回None，或者自己指定的value：
d.get('Thomas')
d.get('Thomas', -1)

#删除一个key ，可以用pop
d.pop('amy')


##字典的迭代
#key迭代
for key in d:
    print key
#key,value迭代
for k,v in d.iteritems():
    print k,v




'''
set 中不存在重复元素
创建set,需要提供一个list输入
'''

s = set([1, 2, 3])
s.add(4)
print s
s.remove(4)
print s



'''
不可变对象：字符串、整数等
可变对象：list..
对可变对象操作，对象内部内容会发生改变
对不可变对象操作，对象本身不会改变
'''

l = [1,3,2,0]
l.sort()
l

s = 'abc'
s.replace('a','A')
s

'''
说明：a是变量，而'abc'才是字符串对象！有些时候，我们经常说，对象a的内容是'abc'，
但其实是指，a本身是一个变量，它指向的对象的内容才是'abc'

当我们调用a.replace('a', 'A')时，实际上调用方法replace是作用在字符串对象'abc'上的，
而这个方法虽然名字叫replace，但却没有改变字符串'abc'的内容。
相反，replace方法创建了一个新字符串'Abc'并返回，
如果我们用变量b指向该新字符串，就容易理解了，变量a仍指向原有的字符串'abc'，但变量b却指向新字符串'Abc'了

'''