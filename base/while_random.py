"""
猜数字游戏
计算机出一个1~100之间的随机数由人来猜
计算机根据人猜的数字分别给出提示大一点/小一点/猜对了
"""
import random
answer = random.randint(1,100);
counter = 0;
while True:
    counter +=1;
    number = int(input('please input:'));
    if(number < answer):
        print("small");
    elif(number > answer):
        print("big");
    else:
        print("vicotr");
        break;
print("Total %d" % counter );
if(counter > 7):
    print("too many");
