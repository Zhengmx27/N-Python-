# -*- coding:utf-8 -*-
import numpy as np
count = 0  #解的个数
size = 0#皇后数目
queen = [0 for i in range(size)]#矩阵

def display():
    global count
    #print("(")
    for i in range(size):
        print(queen[i]+1,end=" ")
    print("\n")
    count = count +1


def Judge_Put(n):
    for i in range(n):
        if(queen[i] == queen[n]):
            return 0
        if(abs(queen[i] - queen[n]) == abs(n - i)):
            return 0
    return 1
#回溯法
def N_Queens(n):
    for i in range(size):
        queen[n] = i #将皇后摆到当前循环到的位置
        if(Judge_Put(n)):
            if(n == size-1):
                display()
            else:
                N_Queens(n+1)

if __name__ == '__main__':

        print("输入N皇后的个数\n")
        size = int(input())
        queen = [0 for i in range(size)]
        N_Queens(0)

        print("一共"+str(count)+"种解法")
