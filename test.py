
def pysim_bar():
    import PySimpleGUI as sg
    import time
    count = range(100)
    for i,item in enumerate(count):
        sg.one_line_progress_meter('实时进度',i + 1,len(count),'-key-')
        time.sleep(0.05)

#with资源管理
def filewith():
    fileList = []
    for i in range(1000):
        with open('test.txt','w') as f:
            fileList.append(f)

'''
上下文管理器可确保用过的资源得到迅速释放，通常和 with 语句一起使用，大大提高了程序的简洁度。
另外需要注意的是，编写基于类或者生成器的上下文管理器时，记住不要忘记释放资源
可以使用 contextlib.contextmanager 装饰器而不使用类的方式来实现上下文管理器，它是基于生成器的上下文管理器，用以支持 with 语句
'''
#@contextmanager 装饰器
from contextlib import contextmanager
@contextmanager
def file_manager(name,mode):
    try:
        f = open(name,mode)
        yield f
    finally:
        f.close()
#实现:
#with file_manager('test.txt','r') as f:
        #f.readline()
'''
*********创建类的迭代器******
一个类作为一个迭代器使用需要在类中实现两个方法 __iter__() 与 __next__() 。
'''
class Mynumber():
    def __iter__(self):
        self.a = 1
        return self
    def __next__(self):
        if self.a < 10:  #迭代次数，要不然for循环会一直执行
            x = self.a
            self.a +=1
            return x
        else:
            raise StopIteration
    '''
    实现:
    myclass = Mynumber()
    myiter = iter(myclass)
    for x in myiter:  # 里也可以直接用对象，因为它的类已经定义iter和next。
        print(x, end=" ")
    '''

"""
******返回n以内的可以被7整除的数
"""
#方法1(不建议使用,常规思维，浪费内存)
def zc(n):
    l = []
    for i in range(n+1):
        if i % 7 ==0:
            l.append(i)
    return l

#方法2(列表推导式)
def zc2(n):
    l = [ x for x in range(n+1) if x % 7 == 0]
    return l

#迭代器fiter
def zc3(n):
    l  = (i for i in range(n+1) if i % 7 == 0)
    return l

#过滤器filter和lambda(推荐方法)
def zc4(n):
    l = filter(lambda x: x % 7 == 0,range(n+1))
    return l

#精确控制循环次数
def zc5(n) -> int : #定义函数时提供类型提示
   l = (i * 7 for i in range(n // 7))
   return l
'''
***列表浅拷贝和深拷贝
'''
def qs():
    a = [1,2,3,4]
    b = a #浅拷贝(b引用a列表)
    b = a.copy() #深拷贝
    b.append(5)
"""
********python 性能提升的几种方法
"""
'''
********Python arrow 更好的日期时间模块
'''
import arrow
def arrow_time():
    now = arrow.now()
    print(now)
    print(now.format())
    print(now.format('YYYY/MM/DD hh:mm:ss'))
    print(now.format('YYYY-MM-DD'))

#队列
from collections import deque
class Queue():
    def __init__(self):
        self.s  = deque()
    def push(self,el):
        self.s.append(el)
    def pop(self):
        return self.popleft()


if __name__ == '__main__':
    #pysim_bar()
    #with file_manager('test.txt','r') as f:
        #f.readline()
    #myclass = Mynumber()
    #myiter = iter(myclass)
    #for x in myiter:  #里也可以直接用对象，因为它的类已经定义iter和next。
        #print(x,end=" ")
    #print(list(zc3(14)))
    #print(list(zc4(14)))
    #print(list(zc5(14)))
    #arrow_time()
    import pprint

