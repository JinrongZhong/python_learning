# -*- coding: utf-8 -*-
"""
Created on Sat Jun 02 17:00:46 2018

@author: ZJR


数据类型检查和异常和异常处理

运行期检测到的错误被称为异常。

"""

# 一、判断输入是否合法

string = raw_input()

string.isalnum()#所有字符都是数字或字母
string.isalpha()#所有字符都是字母
string.isdigit()#所有字符都是数字
string.islower()#所有字符都是小写
string.isupper()#所有字符都是大写



'''
二、异常和异常处理
1. try语句按照如下方式工作；

(1). 首先，执行try子句（在关键字try和关键字except之间的语句）
(2). 如果没有异常发生，忽略except子句，try子句执行后结束。
(3). 如果在执行try子句的过程中发生了异常，那么try子句余下的部分将被忽略。如果异常的类型和 except 之后的名称相符，那么对应的except子句将被执行。最后执行 try 语句之后的代码。
(4). 如果一个异常没有与任何的except匹配，那么这个异常将会传递给上层的try中。
一个 try 语句可能包含多个except子句，分别来处理不同的特定的异常。最多只有一个分支会被执行。
处理程序将只针对对应的try子句中的异常进行处理，而不是其他的 try 的处理程序中的异常。
一个except子句可以同时处理多个异常，这些异常将被放在一个括号里成为一个元组

2. 通常使用raise来抛出异常
'''
try:
    f = float(string)
except ValueError:
    print('输入错误')
    raise#报错
except (RuntimeError, TypeError, NameError):
    pass   
except:
    raise
    
    
#对于函数参数
def function(x):
    if not isinstance(x,(int,float)):#isinstance 判断参数数据类型是否一致
        raise TypeError('bad operand type')
        

'''
三、定义自己的异常
'''