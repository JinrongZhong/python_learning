# -*- coding: utf-8 -*-
"""
Created on Sun Jun 03 13:21:19 2018

@author: ZJR

函数
"""

'''
定义函数：
1.def 定义函数，依次写出函数名，括号，参数，以及冒号
2.在缩进块中编写函数体
3.可以用 return 返回
'''

import math

def nop():
    pass  #空函数


def my_abs_v1(x):
   if x>0:
       return x
   else:
       return -x
   

#增加参数
def my_abs_v2(x):
    if not isinstance(x,(int,float)):
        raise TypeError('bad operand type')
    if x > 0:
        return x
    else:
        return -x
    
#函数可以同时返回多个值，但其实就是一个tuple。调用时用多个变量接收    
def move(x,y,step,angle=0):
    nx = x + step*math.cos(angle)
    ny = y - step*math.sin(angle)
    return nx,ny

nx,ny = move(1,2,3)
r = move(1,2,3)

'''
上面的angle为默认参数，在函数move被调用时，可以传3个参数，也可以传递四个参数
一般把默认参数放在后面
特别注意，默认参数必须指向不变的对象
'''

###可变参数，可变参数就是传入的参数个数是可变的，在函数调用时自动组装为一个tuple
def calc(*number):
    SUM = 0
    for n in number:
        SUM += n
    return SUM

SUM1 = calc(1,2,3,4)
l = [1,2,3,4]
SUM2 = calc(l[0],l[1],l[2],l[3])
SUM3 = calc(*l)

'''
关键字参数，传入的参数个数是可变的，在函数内部自动组装为一个dict
可以只传必选参数，也可以传任意个参数
'''
def person(name, age, **kw):
    print 'name:',name, 'age:',age, 'other:',kw

person('Adam',45)
person('Adam', 45, gender='M')     
person('Adam', 45, gender='M', job='Engineer')    
kw = {'city': 'Beijing', 'job': 'Engineer'}
person('Jack', 24, city=kw['city'], job=kw['job'])
person('jack',24,**kw)


'''
参数组合
在Python中定义函数，可以用必选参数、默认参数、可变参数和关键字参数，这4种参数都可以一起使用，或者只用其中某些，
但是请注意，参数定义的顺序必须是：必选参数、默认参数、可变参数和关键字参数。
'''
def func(a,b,c=0,*args,**kw):
    print 'a:',a , 'b:',b , 'c:',c,'args:',args,'kw',kw
    
args = [1,2,3,4]    
kw = {'city': 'Beijing', 'job': 'Engineer'}    
func(1,2)
func(1,2, 'a', 'b')
func(1,2,'a','b', x = 90)   
func(*args,**kw) 
    
'''
递归函数
在函数内部调用自身本身
'''    
#例如求阶乘
def fact(n):
    if n == 1:
        return 1
    return n*fact(n-1)


'''
在计算机中，函数调用是通过栈实现的，每当进入一个函数调用，栈就会加一层栈帧，每当函数返回，栈就会减一层栈帧，
由于栈的大小是有限的，所以当递归调用的次数过多，会导致栈溢出

可以通过尾递归优化来解决
尾递归是指在函数结束时调用自身本身，并且，return语句不能含有表达式
这样，编译器或者解释器就可以把尾递归做优化，使递归本身无论调用多少次，都只占用一个栈帧，不会出现栈溢出的情况。
大多数编程语言没有针对尾递归做优化，Python解释器也没有做优化，所以还是会溢出
'''
def fact_v2(n):
    return fact_iter(n,1)

def fact_iter(num,product):
    if num == 1:
        return product
    return fact_iter(num-1 , num*product)


fact_v2(1000)









