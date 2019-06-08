from random import randint

#默认值 2
def roll_dice(n=2):
    """
    摇色子
    
    :param n: 色子的个数
    :return: n颗色子点数之和
    """
    total = 0
    for _ in range(n):
        total += randint(1, 6)
    return total


#默认值 0， 0， 0
def add(a=0, b=0, c=0):
    return a + b + c


# 如果没有指定参数那么使用默认值摇两颗色子
print("roll_dice()",roll_dice())
# 摇三颗色子
print("roll_dice(3)",roll_dice(3))
print("add()",add())
print("add(1)",add(1))
print("add(1, 2)",add(1, 2))
print("add(1, 2, 3)",add(1, 2, 3))
# 传递参数时可以不按照设定的顺序进行传递
print("add(c=50, a=100, b=200)",add(c=50, a=100, b=200))
