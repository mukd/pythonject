"""
***
python 多态 协议 鸭子类型详解
****
"""
from abc import abstractmethod,ABCMeta
#鸭子类
class Dock(metaclass=ABCMeta):
    @abstractmethod
    def Swimming(self):  #游泳方法协议(接口)
        pass

    @abstractmethod
    def Wall(self): #走路协议(接口)
        pass

    @classmethod
    def __subclasshook__(cls,C):
        # 判断是否另一个比较类是否实现了 Swimming Walk 协议， 如果实现了鸭子类的这两个协议，
        # 那么比较类的类型就是一个鸭子类型
        # 当代码执行中如果执行到对象和这个类进行 isinstance 类型判断时会走到这个函数进行判断
        for method in  ('Swimming','Wall'):
            for B in C.__mro__:
                if method in B.__dict__:
                    if B.__dict__[method] is None:
                        return NotImplemented
                    break
            else:
                return NotImplemented
        return True

#狗类
class Dog(object):
    # 实现swimming 协议
    def Swimming(self):
        print('狗会狗刨！')
    #实现walk协议
    def Wall(self):
        print('狗会走路！')
    def Eat(self):
        print('狗喜欢吃骨头！')

#乌龟类
class Tortoise(object):
    # 实现swimming 协议
    def Swimming(self):
        print("乌龟会潜水")
    # 实现walk 协议
    def Wall(self):
        print("乌龟会走路")
    def Eat(self):
        print("乌龟喜欢吃鱼")

if __name__ == '__main__':
    dg = Dog()
    te = Tortoise()
    print(isinstance(dg,Dock))
    print(isinstance(te,Dock))
    '''
    说明:
    可以看到，在上面的代码中，只要实现了 Dock 类中的 swimming 和 Walk 方法，那么这个类就可以被叫做 Dock 类
    应用场景 如： for 循环， 在python 中 for 循环只能用于可迭代对象， 那么， 我自己定义的类实现了 __iter__协议（接口），
    这个实例类就是一个可迭代对象，可以被for 循环使用
    '''




