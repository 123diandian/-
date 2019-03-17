import numpy
import random
import string
from fractions import Fraction


##两个整数的四则运算
def c1(q, ans):
    symbol = random.choice(['+', '-', '*', '/'])  # 生成随机符号
    if symbol == '+':
        n1 = random.randint(0, 100)
        n2 = random.randint(0, 100)
        q.append(str(n1) + '+' + str(n2) + '=')
        ans.append(n1 + n2)
    elif symbol == '-':
        n1 = random.randint(0, 100)
        n2 = random.randint(0, n1 + 1)
        q.append(str(n1) + '-' + str(n2) + '=')
        ans.append(n1 - n2)
    elif symbol == '*':
        n1 = random.randint(0, 100)
        n2 = random.randint(0, 100)
        q.append(str(n1) + '×' + str(n2) + '=')
        ans.append(n1 * n2)
    else:
        n1 = random.randint(0, 100)
        if n1 == 0:
            n2 = random.randint(1, 100)
        else:
            n2 = random.randint(1, n1 + 1)
            while n1 % n2:
                n1 = random.randint(1, 100)
                n2 = random.randint(1, n1 + 1)
        q.append(str(n1) + '÷' + str(n2) + '=')
        ans.append(Fraction(n1, n2))


##随机生成两个真分数
def createF():
    fz1 = random.randint(0, 100)
    if fz1 == 0:
        fm1 = random.randint(1, 100)
    else:

        fm1 = random.randint(fz1, 100)
    f1 = Fraction(fz1, fm1)
    fz2 = random.randint(1, 100)
    fm2 = random.randint(fz2, 100)
    f2 = Fraction(fz2, fm2)
    return f1, f2

##两个真分数的四则运算
def c2(q,ans):
    symbol = random.choice(['+','-','*','/'])
    f1,f2 = createF()
    if symbol =='+':
        while f1+f2>1:
            f1,f2 = createF()
        q.append(str(f1)+'+'+str(f2)+'=')
        ans.append(f1+f2)
    elif symbol =='-':
        f1,f2 = max(f1,f2),min(f1,f2)
        q.append(str(f1)+'-'+str(f2)+'=')
        ans.append(f1-f2)
    elif symbol == '*':
        while f1*f2>1:
            f1,f2 = createF()
        q.append(str(f1)+'×'+str(f2)+'=')
        ans.append(f1*f2)
    else:
        while f1/f2>1:
            f1,f2=createF()
        q.append(str(f1)+'÷'+str(f2)+'=')
        ans.append(Fraction(f1,f2))


while 1:
    print("输入类型序号： 1.测试  2.练习  3.退出")
    t = int(input())
    if t == 3:
        break
    elif t == 1:  ##测试
        print("输入想要的四则运算序号： 1.整数  2.真分数  3.混合  4.退出")
        n = int(input())
        while n > 4:
            print("输入有误，重新输入")
            n = int(input())
        if n == 4:
            break
        print("输入题目的数量", end='  ')
        k = int(input())
        p = 100 / k
        s = 0
        q = []
        ans = []
        if n == 1:  ##整数测试
            for i in range(k):
                c1(q, ans)
        elif n == 2:  ##分数测试
            for i in range(k):
                c2(q, ans)
        elif n == 3:  ##混合测试
            for i in range(k):
                n = random.randint(1, 3)
                if n == 1:
                    c1(q, ans)
                else:
                    c2(q, ans)
        for i in range(k):
            print("第{}题：{}".format(i + 1, q[i]), end='  ')
            a = input()
            if a == str(ans[i]):
                s = s + p
        print("所得的分数为：{}".format(s))
        print("是否查看正确答案：1.是  2.否", end='   ')
        da = int(input())
        if da == 1:
            for i in range(k):
                print(q[i] + str(a[i]))



    elif t == 2:  ##练习
        print("输入想要的四则运算序号： 1.整数  2.真分数  3.混合  4.退出")
        n = int(input())
        while n > 4:
            print("输入有误，重新输入")
            n = int(input())
        if n == 4:
            break
        print("输入题目的数量", end='  ')
        k = int(input())
        q = []
        ans = []
        if n == 1:
            for i in range(k):
                c1(q, ans)
        elif n == 2:
            for i in range(k):
                c2(q, ans)
        elif n == 3:
            for i in range(k):
                n = random.randint(1, 3)
                if n == 1:
                    c1(q, ans)
                else:
                    c2(q, ans)
        else:
            print("输入有误！请重新输入")

        for i in range(k):
            print("第{}题：{}".format(i + 1, q[i]), end='  ')
            a = input()
            if a == str(ans[i]):
                print("回答正确")
            else:
                print("回答错误，正确答案是：{}".format(ans[i]))
    else:
        print("输入有误！请重新输入")